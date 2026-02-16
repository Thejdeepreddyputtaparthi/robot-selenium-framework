*** Settings ***
Library    SeleniumLibrary
*** Settings ***
Library    libraries.core.browser_manager.BrowserManager
Library    libraries.pages.login_page.LoginPage
Library    libraries.utils.faker_library.FakerLibrary

Variables  ../config/variables.py
Test Setup      Open Application
Test Teardown   Close Application

*** Test Cases ***
Valid Login
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASSWORD}
    Verify Inventory Page

Invalid Login - Wrong Username
    Go To Login Page
    Login With Credentials    ${INVALID_USER}    ${VALID_PASSWORD}
    Verify Error Message    Epic sadface: Username and password do not match any user in this service

Invalid Login - Wrong Password
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${INVALID_PASSWORD}
    Verify Error Message    Epic sadface: Username and password do not match any user in this service

Empty Username
    Go To Login Page
    Login With Credentials   ${EMPTY}      ${VALID_PASSWORD}
    Verify Error Message    Epic sadface: Username is required

Empty Password
    Go To Login Page
    Login With Credentials    ${VALID_USER}   ${EMPTY}
    Verify Error Message    Epic sadface: Password is required

Locked Out User
    Go To Login Page
    Login With Credentials    ${LOCKED_USER}    ${VALID_PASSWORD}
    Verify Error Message    Epic sadface: Sorry, this user has been locked out.

Invalid Login - Random Username
    ${random_user}=    Random Username
    Go To Login Page
    Login With Credentials    ${random_user}    ${VALID_PASSWORD}
    Verify Error Message    Epic sadface: Username and password do not match any user in this service

Invalid Login - Random Password
    ${random_pass}=    Random Password
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${random_pass}
    Verify Error Message    Epic sadface: Username and password do not match any user in this service

