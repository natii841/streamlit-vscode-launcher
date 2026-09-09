import os
import subprocess
import streamlit as st
from PIL import Image

# Page Configuration
st.set_page_config(
    page_title="VS Code Folder Opener",
    page_icon="⚡",
    layout="centered"
)

# Custom CSS for cleaner UI
st.markdown("""
    <style>
    .main-header { font-size: 2.2rem; font-weight: 700; margin-bottom: 0.5rem; }
    .sub-text { color: #6c757d; font-size: 1rem; margin-bottom: 1.5rem; }
    .stButton>button { width: 100%; border-radius: 8px; font-weight: 600; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">⚡ Quick Folder Launcher</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-text">Navigate directories and preview files before opening in VS Code.</div>', unsafe_allow_html=True)

# Initialize Session State
if "current_dir" not in st.session_state:
    st.session_state.current_dir = os.path.expanduser("~")

current_dir = st.session_state.current_dir

# --- QUICK JUMP BAR ---
st.caption("📌 Quick Locations")
q_col1, q_col2, q_col3, q_col4 = st.columns(4)

with q_col1:
    if st.button("🏠 Home"):
        st.session_state.current_dir = os.path.expanduser("~")
        st.rerun()

with q_col2:
    if st.button("💻 Desktop"):
        desktop = os.path.join(os.path.expanduser("~"), "Desktop")
        if os.path.exists(desktop):
            st.session_state.current_dir = desktop
            st.rerun()

with q_col3:
    if st.button("📄 Documents"):
        docs = os.path.join(os.path.expanduser("~"), "Documents")
        if os.path.exists(docs):
            st.session_state.current_dir = docs
            st.rerun()

with q_col4:
    if st.button("⬇️ Downloads"):
        downloads = os.path.join(os.path.expanduser("~"), "Downloads")
        if os.path.exists(downloads):
            st.session_state.current_dir = downloads
            st.rerun()

st.divider()

# --- CURRENT PATH DISPLAY & PRIMARY ACTION ---
st.subheader("Current Location")
st.code(current_dir, language="bash")

col_open, col_up = st.columns([3, 1])

with col_open:
    if st.button("🚀 OPEN THIS FOLDER IN VS CODE", type="primary"):
        try:
            subprocess.run(["code", current_dir], check=True, shell=True)
            st.toast("Opened successfully in VS Code!", icon="✅")
        except Exception as e:
            st.error(f"Could not open VS Code: {e}")

with col_up:
    parent_dir = os.path.dirname(current_dir)
    if parent_dir and parent_dir != current_dir:
        if st.button("⬆️ Up Level"):
            st.session_state.current_dir = parent_dir
            st.rerun()

st.divider()

# --- SUBDIRECTORY EXPLORER WITH SEARCH ---
st.subheader("Subfolders")

try:
    all_entries = os.listdir(current_dir)
    subdirs = [
        d for d in all_entries
        if os.path.isdir(os.path.join(current_dir, d)) and not d.startswith(".")
    ]
    files = [
        f for f in all_entries
        if os.path.isfile(os.path.join(current_dir, f)) and not f.startswith(".")
    ]
    subdirs.sort()
    files.sort()
except PermissionError:
    st.error("🚫 Access denied for this folder.")
    subdirs, files = [], []

if subdirs:
    search_query = st.text_input("🔍 Filter folders by name...", "")
    filtered_dirs = [d for d in subdirs if search_query.lower() in d.lower()] if search_query else subdirs

    if filtered_dirs:
        selected_folder = st.radio(
            "Select a folder to enter:",
            options=filtered_dirs,
            index=0,
            key="folder_select"
        )
        if st.button("➡️ Enter Selected Folder"):
            st.session_state.current_dir = os.path.join(current_dir, selected_folder)
            st.rerun()
    else:
        st.info("No matching folders found.")
else:
    st.info("No subfolders in this directory.")

st.divider()

# --- NEW: FILE LIST VIEWER & PREVIEW ---
st.subheader("📄 Files in this Folder")

if files:
    st.caption(f"Total Files: {len(files)}")
    
    # Select a file to inspect
    selected_file = st.selectbox("Select a file to preview:", options=["-- Select a file --"] + files)
    
    if selected_file != "-- Select a file --":
        file_path = os.path.join(current_dir, selected_file)
        file_size = os.path.getsize(file_path) / 1024  # Size in KB
        
        st.caption(f"File Size: {file_size:.2f} KB")
        
        # File preview logic based on extension
        ext = os.path.splitext(selected_file)[1].lower()
        
        if ext in [".py", ".json", ".txt", ".md", ".sh", ".js", ".html", ".css", ".yml"]:
            try:
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read(2000)  # Read first 2000 characters
                st.code(content, language="python" if ext == ".py" else "text")
            except Exception as e:
                st.error(f"Unable to read text file: {e}")
                
        elif ext in [".png", ".jpg", ".jpeg", ".webp"]:
            try:
                image = Image.open(file_path)
                st.image(image, caption=selected_file, use_container_width=True)
            except Exception as e:
                st.error(f"Unable to render image: {e}")
        else:
            st.info("Preview not available for this file type.")
else:
    st.info("No files in this directory.")