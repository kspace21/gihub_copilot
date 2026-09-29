# GitHub Copilot System Uptime Script Task

## 1. Generated Code by Copilot
Initially, Copilot generated a simple script using `os.popen('uptime').read()`.

## 2. Code Modifications & Improvements
I refactored the script to improve security and reliability:
- **Security:** Replaced `os.popen()` with `subprocess.run()` to avoid shell injection vulnerabilities.
- **Error Handling:** Added `try-except` blocks to handle command errors gracefully (e.g., if running on unsupported OS like Windows without WSL).
- **Structure:** Wrapped the logic inside a function (`get_system_uptime()`).

## 3. How to Run
Run the script using Python 3:
```bash
python copilot_test.py
