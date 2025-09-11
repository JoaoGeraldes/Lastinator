# Lastinator (last file copier)

A small Windows desktop app that copies the _most recently modified file_ from a source folder to a destination folder when you press a button.

---

## 🔎 What it does

- Lets the user enter a **From (source)** folder and a **To (destination)** folder in the UI.
- When **Copy Last File** is clicked, the app finds the most recently modified file in the source folder and copies it to the destination folder.
- Shows popup messages for success, warnings, and errors.

---

## 🧾 Prerequisites

- Windows 10/11
- Python 3.10+ installed (download from [https://www.python.org](https://www.python.org) if needed)

  - Make sure your Python installation includes `tkinter` (the standard Windows installers include it).

---

## 🛠 Development — Setup on Windows (recommended)

These steps create and use a virtual environment so you don't install anything into the global Python environment.

### 1. Clone or copy the project

```powershell
git clone https://github.com/JoaoGeraldes/Lastinator.git

cd Lastinator
```

(Or simply copy the files into a folder.)

### 2. Create a virtual environment

```powershell
python -m venv venv
```

This creates a `venv` folder in your project.

### 3. Activate the virtual environment

**PowerShell** (recommended):

```powershell
# If running PowerShell
.\venv\Scripts\Activate.ps1
```

**Command Prompt (cmd.exe):**

```cmd
venv\Scripts\activate
```

**Git Bash / WSL-like shells:**

```bash
source venv/Scripts/activate
```

When the environment is active you should see `(venv)` at the start of your prompt.

> If PowerShell blocks running the activation script due to execution policy, you can run PowerShell as Administrator once and set the policy for your user: `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`. Only do this if you understand the security implications.

### 4. Install requirements (if any)

This project uses only the Python standard library, so there are **no external requirements by default**. If you extend the project and add third-party packages, record them in `requirements.txt` and install with:

```powershell
pip install -r requirements.txt
```

You can create a `requirements.txt` from your environment with:

```powershell
pip freeze > requirements.txt
```

---

## ▶️ Run the application

With the virtual environment activated:

```powershell
python main.py
```

Notes:

- The source folder must exist and contain at least one file.
- The destination folder must already exist (the app will not create it automatically).

---

## 📦 Build a single `.exe` (Optional)

If you want to distribute the app to machines without Python installed, create a standalone executable using **PyInstaller**.

1. Install PyInstaller inside the activated venv:

```powershell
pip install pyinstaller
```

2. Build the .exe (windowed, single file):

```powershell
pyinstaller --onefile --windowed file_copier.py
```

3. The built executable will be at `dist/main.exe`.

> Test the `.exe` on a machine similar to your target environment to ensure it bundles everything correctly.

---

## ⚙️ Troubleshooting

- **`tkinter` import error**: Make sure you installed Python from the official installer (not every Python distribution includes Tk). Reinstall Python using the installer from python.org and ensure "tcl/tk and IDLE" is selected.

- **Activation blocked on PowerShell**: See note above about `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`.

- **No files in source**: The app will show a warning popup. Verify you pointed the `From` field to a folder that contains at least one file.

- **Permissions**: Make sure you have read permission for the source folder and write permission for the destination folder.

## 📁 Example `requirements.txt`

This project does not require external packages by default. If you add packages, an example `requirements.txt` might look like:

```
# Example (uncomment if you add third-party packages)
# pyinstaller==5.9.0
```

Create it with `pip freeze > requirements.txt` once you install any packages inside the venv.
