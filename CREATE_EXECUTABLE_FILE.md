# Build a Windows Executable from Python (Tkinter App)

Turn your Python project into a standalone `.exe` using **PyInstaller**.

---

## 1️⃣ Install PyInstaller

```bash
pip install pyinstaller
```

---

## 2️⃣ Prepare your project

- Make sure your main script is clean, e.g., `main.py`.
- Include any resources like `icon.png` or `style.json` in the same folder (or note the paths).

Example project structure:

```
Lastinator/
  ├── main.py
  ├── style.json
  └── icon.png
```

---

## 3️⃣ Create the executable

From your project folder, run:

```bash
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

### Flags explained

| Flag              | Purpose                                            |
| ----------------- | -------------------------------------------------- |
| `--onefile`       | Packs everything into a single `.exe`              |
| `--windowed`      | Hides the console (good for GUI apps)              |
| `--icon=icon.ico` | Sets the executable icon (Windows requires `.ico`) |

---

## 4️⃣ Locate your executable

After running PyInstaller, check the `dist` folder inside your project.

You’ll find:

```
dist/
  └── main.exe
```

(or `Lastinator.exe` if you renamed the script).

---

## 5️⃣ Include external files (like `style.json`)

By default, PyInstaller only bundles Python code. If your app needs files:

### Option A: Copy manually

Place `style.json` in the same folder as the `.exe`:

```
dist/
  ├── main.exe
  ├── style.json
  └── icon.png
```

### Option B: Use `--add-data`

```bash
pyinstaller --onefile --windowed --icon=icon.ico --add-data "style.json;." main.py
```

📌 **Syntax:** `"source_path;destination_path_inside_exe"`  
👉 Use `:` instead of `;` on macOS/Linux

---

## 6️⃣ Run your executable

Double-click `main.exe` → your Tkinter app runs like a native app.

✅ The window has your icon, inputs, button, and styling.

---

## 💡 Tips

- Test the `.exe` on a **clean Windows machine** to ensure no dependencies are missing.
- For macOS, use a similar tool like **py2app**.

---
