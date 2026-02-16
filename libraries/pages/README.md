# SDET Automation Project

## Overview
This project demonstrates automation testing using **Robot Framework**, **Python**, and **Selenium** for web UI automation. It covers **login**, **cart**, and negative/edge-case scenarios with dynamic test data generated via **Faker**. The framework is designed following **Page Object Model** principles and supports **multi-browser** and **headless execution** using a `DriverFactory`.

The project is organized for **maintainability, scalability, and reusability**, suitable for technical exercises or enterprise-level SDET demonstrations.

---

## Project Structure

ROBOT-SELENIUM-FRAMEWORK/
│
├── tests/ # Robot Framework test cases
│ ├── login_tests.robot
│ ├── cart_tests.robot
│
├── libraries/ # Custom Python libraries
│ ├── core/
│ │ ├── browser_manager.py # Browser management using DriverFactory
│ ├── pages/
│ │ ├── login_page.py
│ │ ├── inventory_page.py
│ └── utils/
│ └── faker_library.py # Faker-based dynamic test data
│
├── config/
│ └── variables.py # Centralized test data (usernames, passwords, products)
├── requirements.txt # Python dependencies
├── README.md
└── reports/ # Test reports and logs


---

## Key Features

1. **Page Object Model (POM):**
   - Separate classes for `LoginPage` and `InventoryPage`.
   - Encapsulates actions like login, add/remove products, and cart verification.

2. **Faker Integration:**
   - Dynamic generation of invalid usernames, passwords, and products for negative test scenarios.

3. **BrowserManager:**
   - Supports **Chrome** browsers.
   - Supports **headless execution** for CI/CD pipelines.
   - Centralized driver management in `BrowserManager`.

4. **Data-Driven Tests:**
   - All test data (credentials, products) stored in `variables.py`.
   - Easily extensible for additional scenarios.

5. **Edge Cases & Negative Tests:**
   - Invalid login credentials
   - Locked out users
   - Empty fields
   - Adding nonexistent products to cart

6. **Scalable & Maintainable:**
   - Modular framework structure allows adding new pages and tests quickly.
   - Clean separation of test logic and browser handling.

---

## Setup Instructions

1. **Clone the Repository**

git clone <your-repository-url>
cd robot-selenium-framework
Create Python Virtual Environment

python -m venv venv
Activate the Virtual Environment

# Windows
venv\Scripts\activate

# Linux / Mac
source venv/bin/activate
Install Dependencies

pip install -r requirements.txt

RunningTests
Run All Tests
robot  tests/

Run Specific Test File
robot tests/login_tests.robot
robot tests/cart_tests.robot

Run with Specific Browser / Headless Mode
robot -v BROWSER:chrome -v HEADLESS:True tests/
robot -v BROWSER:firefox -v HEADLESS:False tests/


TestReports

Output XML: output/output.xml

HTML Log: output/log.html

HTML Report: output/report.html

All reports are automatically generated after test execution.
