# ⚡ Streamlit VS Code Directory Launcher

An interactive local directory navigator and file previewer built with Streamlit. Easily browse your local file system, inspect file contents, and open selected project folders directly in Visual Studio Code with a single click.

---

## ✨ Features

- **📌 Quick Location Jumps:** One-click shortcuts to navigate to `Home`, `Desktop`, `Documents`, and `Downloads`.
- **📂 Interactive Folder Navigation:** Browse through subdirectories level-by-level with a filter search bar.
- **📄 File Previewer:** View code, text files (`.py`, `.json`, `.md`, `.txt`, etc.), and images (`.png`, `.jpg`, `.webp`) inline along with file size indicators.
- **🚀 VS Code Integration:** Launch the current directory directly in Visual Studio Code from the browser interface.

---

## 🛠️ Prerequisites

- **Python 3.8+**
- **Visual Studio Code** installed and added to your system `PATH` (so the `code` CLI command is available).

---

## 🚀 Quick Start (Local Setup)

1. **Clone the repository:**



2. **Create and activate a virtual environment:**
* **Windows (PowerShell):**
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1

```


* **macOS / Linux:**
```bash
python3 -m venv .venv
source .venv/bin/activate

```




3. **Install dependencies:**
```bash
pip install -r requirements.txt

```


4. **Run the Streamlit app:**
```bash
streamlit run app.py

```



---

## ⚠️ Usage Note

This app is designed to run **locally** on your personal computer. Running it locally gives Streamlit access to your system's file system and allows it to trigger the local `code` command to launch VS Code desktop instances.

---

## 📄 License

This project is open source and available under the [MIT License](https://www.google.com/search?q=LICENSE).

```

---

### How to Add This to Your Repository

1. Open your `Streamlit` project folder in VS Code.
2. Create a new file named **`README.md`**.
3. Paste the markdown code above into the file.
4. Replace `YOUR_USERNAME` in the clone link with your actual GitHub username and save (`Ctrl + S`).

<FollowUp label="Would you like help generating a license file (e.g., MIT) or .gitignore for this project?" query="How do I create a .gitignore and LICENSE file for my Python Streamlit project?"/>

```
