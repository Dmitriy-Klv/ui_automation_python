# UI Automation Tests (Playwright + Pytest)

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-1.48+-blue)](https://playwright.dev/python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project is a sample UI test automation framework built with **Python**, **Playwright**, and **Pytest**.
It demonstrates a clean Page Object Model (POM) architecture and is intended for learning, practice,
and portfolio purposes.

## 🔧 Tech Stack
- Python 3.12+
- Playwright (sync API)
- Pytest
- Page Object Model (POM)

## 📁 Project Structure
.
├── .env
├── conftest.py
├── requirements.txt
├── README.md
├── LICENSE.txt          
├── pages/
│   ├── base_page.py
│   ├── inventory_page.py
│   └── login_page.py
├── config/
│   └── settings.py
└── tests/
    └── tests.py


## ▶️ How to Run Tests
1. Create virtual environment:
```bash
python -m venv .venv
```

2. Activate virtual environment:
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate
# macOS / Linux
python -m venv .venv
source .venv/bin/activate
```
3. Install dependencies:
```bash
pip install -r requirements.txt
playwright install
```
4. Run tests:
```bash
pytest
```

🌐 Tested Application
Tests are executed against the public demo site:
https://www.saucedemo.com
This site is provided by Sauce Labs for testing and educational purposes.

⚠️ Disclaimer
This project is for educational and demonstration purposes only.

📄 License
This project is licensed under the MIT License.


