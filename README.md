# Guides

### 1. Setting Up Your Environment

#### Install Python
Make sure you have Python installed on your machine. You can download it from [python.org](https://www.python.org/).

#### Create a Virtual Environment
It's good practice to use a virtual environment for your project.

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### 2. Install Playwright and Allure

#### Install Playwright
You can install Playwright using pip.

```bash
pip install playwright
```

#### Install Allure Pytest
Allure Pytest is required for generating the reports.

```bash
pip install allure-pytest
```

#### Install Allure Command Line
Follow the instructions to install Allure Command Line from [the official Allure website](https://docs.qameta.io/allure/#_get_started).

For example, on macOS using Homebrew:

```bash
brew install allure
```

On Windows, download the binary from the [official site](https://docs.qameta.io/allure/#_get_started) and add it to your PATH.

### 3. Initialize Playwright

You need to install the necessary browser binaries.

```bash
python -m playwright install
```

### 4. Write Your First Test

Create a new directory for your tests, e.g., `tests`. Inside this directory, create a file called `test_example.py` with the following content:

```python
import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        yield browser
        browser.close()

def test_example(browser):
    page = browser.new_page()
    page.goto("https://example.com")
    assert page.title() == "Example Domain"
```

### 5. Configure Allure

Create a file named `pytest.ini` in your project root with the following content:

```ini
[pytest]
addopts = --alluredir=allure-results
```

### 6. Run Your Tests

Run your tests using pytest. This will generate the results for Allure.

```bash
pytest
```

### 7. Generate and Open Allure Report

Generate the Allure report using the following command:

```bash
allure serve allure-results
```

This will start a local server and open the Allure report in your default web browser.

### Summary

1. **Set up Python environment:**
   - Create a virtual environment.
   - Install Playwright and Allure Pytest using pip.
   - Install Allure Command Line.

2. **Initialize Playwright:**
   - Install necessary browser binaries.

3. **Write test cases:**
   - Use Playwright's API to create and run browser tests.
   - Configure Allure to generate test reports.

4. **Run tests and generate reports:**
   - Use pytest to run tests.
   - Use Allure to generate and view reports.
