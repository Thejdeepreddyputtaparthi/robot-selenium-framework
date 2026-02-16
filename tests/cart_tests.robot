*** Settings ***
Library    SeleniumLibrary
Library    libraries.core.browser_manager.BrowserManager
Library    libraries.pages.login_page.LoginPage
Library    libraries.pages.inventory_page.InventoryPage
Variables  ../config/variables.py

Test Setup    Open Application
Test Teardown   Close Application

*** Test Cases ***

Remove Product From Cart
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASSWORD}
    Add Product To Cart    ${PRODUCT_BACKPACK}
    Go To Cart
    Remove Product From Cart    ${PRODUCT_BACKPACK}
    Should Not See Product In Cart    ${PRODUCT_BACKPACK}

Add Multiple Products To Cart
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASSWORD}
    Add Product To Cart    ${PRODUCT_BACKPACK}
    Add Product To Cart    ${PRODUCT_BIKE_LIGHT}
    Go To Cart
    Should See Product In Cart    ${PRODUCT_BACKPACK}
    Should See Product In Cart    ${PRODUCT_BIKE_LIGHT}

Remove One Product From Cart
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASSWORD}
    Add Product To Cart    ${PRODUCT_BACKPACK}
    Add Product To Cart    ${PRODUCT_BIKE_LIGHT}
    Go To Cart
    Remove Product From Cart    ${PRODUCT_BACKPACK}
    Should Not See Product In Cart    ${PRODUCT_BACKPACK}
    Should See Product In Cart    ${PRODUCT_BIKE_LIGHT}

Empty Cart After Removing All Products
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASSWORD}
    Add Product To Cart    ${PRODUCT_BACKPACK}
    Add Product To Cart    ${PRODUCT_BIKE_LIGHT}
    Go To Cart
    Remove Product From Cart    ${PRODUCT_BACKPACK}
    Remove Product From Cart    ${PRODUCT_BIKE_LIGHT}
    Cart Should Be Empty

Add All Products And Remove One
    Go To Login Page
    Login With Credentials    ${VALID_USER}    ${VALID_PASSWORD}
    FOR    ${product}    IN    @{ALL_PRODUCTS}
        Add Product To Cart    ${product}
    END
    Go To Cart
    Remove Product From Cart    ${PRODUCT_BIKE_LIGHT}
    Should Not See Product In Cart    ${PRODUCT_BIKE_LIGHT}
    Should See Product In Cart    ${PRODUCT_BACKPACK}
    Should See Product In Cart    ${PRODUCT_BOLT_TSHIRT}
