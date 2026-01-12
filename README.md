# UI Automation Tests (Playwright + Pytest)

[![Python](https://img.shields.io/badge/python-3.12+-blue.svg)](https://www.python.org/)  
[![Playwright](https://img.shields.io/badge/Playwright-1.48+-blue)](https://playwright.dev/python/)  
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

This project is a robust **UI test automation framework** built with **Python**, 
**Playwright (sync API)**, and **Pytest**, following the **Page Object Model (POM)** architecture. 
It serves as an educational example, practice tool, and portfolio showcase. Tests are executed against 
the public demo site: [https://www.saucedemo.com](https://www.saucedemo.com).  

The framework includes:  
- Advanced reporting with **Allure**  
- **CI/CD integration** via GitHub Actions  
- Environment configuration management using **Python-dotenv** and **Pydantic-settings**  
## 🔧 Tech Stack
- Python 3.11+  
- Playwright (synchronous API for UI automation)  
- Pytest (with fixtures and plugins)  
- Allure (detailed test reports with history, trends, attachments)  
- Pytest-HTML (basic HTML reports)  
- Python-dotenv & Pydantic-settings (secure and structured configuration management)  
- GitHub Actions (CI/CD with automated test runs and report deployment)

## 📁 Project Structure
```text
├── .env                          # Environment variables (e.g., credentials)
├── .gitignore                    # Git ignore rules
├── conftest.py                   # Global Pytest fixtures (browser setup)
├── LICENSE                       # MIT License
├── pytest.ini                    # Pytest configuration
├── README.md                     # Project README file
├── requirements.txt              # Project dependencies
├── .github/
│   └── workflows/
│       └── allure-report.yml     # GitHub Actions workflow for CI/CD and Allure reports
├── config/
│   └── settings.py               # App settings loaded from .env via Pydantic
├── pages/                        # Page Object Model classes
│   ├── __init__.py
│   ├── base_page.py              # Base class with common page methods
│   ├── cart_page.py              # Cart page interactions
│   ├── checkout_complete_page.py # Checkout completion page
│   ├── checkout_page.py          # Checkout info page
│   ├── CheckoutOverviewPage.py   # Checkout overview page
│   ├── inventory_page.py         # Inventory/products page
│   └── login_page.py             # Login page
└── tests/                        # Test cases and fixtures
    ├── __init__.py
    ├── conftest.py               # Local fixtures (e.g., playwright_page)
    └── tests_ui.py               # UI test cases
```

## ▶️ How to Run Tests Locally

### 1️⃣ Create and activate a virtual environment
```bash
python -m venv .venv

# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```
### 2️⃣ Install dependencies

```
pip install -r requirements.txt
```
### 3️⃣ Install Playwright browsers
```
playwright install
```
### 4️⃣ Run tests
```
# Basic run
pytest

# With Allure results
pytest --alluredir=allure-results

# Serve local Allure report
allure serve allure-results
```

## 🚀 CI/CD and Reporting

### GitHub Actions Workflow
- Workflow file: `.github/workflows/allure-report.yml`  
- Triggers: on push or pull request to `main` branch  
- Features: installs dependencies, runs tests with Allure, generates reports, deploys to GitHub Pages  
- View CI runs: **Actions tab** in GitHub  

### Allure Reports
- Detailed reports with history, trends, and attachments  
- Live report: [https://dmitriy-klv.github.io/ui_automation_python/](https://dmitriy-klv.github.io/ui_automation_python/)  
- Latest report deployed automatically after each CI run

## 🌐 Tested Application
Tested Application Tests are executed against the public demo site: https://www.saucedemo.com
This site is provided by Sauce Labs for testing and educational purposes. 

## ⚠️ Disclaimer
This project is for **educational, practice, and demonstration purposes only**.  
Do not use in production without further validation.  

## 📄 License
This project is licensed under the **MIT License** – see `LICENSE` file for details.











