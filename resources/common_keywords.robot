*** Settings ***
Library    libraries/core/browser_manager.py    WITH NAME    BrowserManager
Library    libraries/pages/login_page.py
Library    libraries/pages/inventory_page.py
Library    libraries/utils/data_generator.py

*** Keywords ***
Launch Application
    Open Application

Close App
    Close Application
