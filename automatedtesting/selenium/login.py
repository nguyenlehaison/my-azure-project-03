# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    options = ChromeOptions()
    options.add_argument('--no-sandbox')
    options.add_argument("--headless") 
    driver = webdriver.Chrome(options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element_by_css_selector("input[id='user-name']").send_keys(user)
    driver.find_element_by_css_selector("input[id='password']").send_keys(password)
    driver.find_element_by_id("login-button").click()
    product_label = driver.find_element_by_css_selector("div[class='product_label']").text
    assert "Products" in product_label
    print(timestamp() + 'Login with username {:s} and password {:s} successfully.'.format(user, password))

def add_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"  # Get the URL of the product
        driver.find_element_by_css_selector(element).click()  # Click the URL
        driver.find_element_by_css_selector("button.btn_primary.btn_inventory").click()  # Add the product to the cart
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text  # Get the name of the product from the page
        print(timestamp() + product + " added to shopping cart.")  # Display message saying which product was added
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()  # Click the Back button
    print(timestamp() + '{:d} items are all added to shopping cart successfully.'.format(n_items))

def remove_cart(driver, n_items):
    for i in range(n_items):
        element = "a[id='item_" + str(i) + "_title_link']"
        driver.find_element_by_css_selector(element).click()
        driver.find_element_by_css_selector("button.btn_secondary.btn_inventory").click()
        product = driver.find_element_by_css_selector("div[class='inventory_details_name']").text
        print(timestamp() + product + " removed from shopping cart.")  # Display message saying which product was added
        driver.find_element_by_css_selector("button.inventory_details_back_button").click()

if __name__ == "__main__":
    number_item = 10
    username = 'standard_user'
    password = 'secret_sauce'
    driver = login( username, password )
    add_cart(driver, N_ITEMS)
    remove_cart(driver, N_ITEMS)