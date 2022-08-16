# #!/usr/bin/env python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


# Start the browser and login with standard_user
def login (user, password):
    print ('Starting the browser...')
    # --uncomment when running in Azure DevOps.
    options = ChromeOptions()
    options.add_argument("--headless") 
    # driver = webdriver.Chrome(options=options)
    chromedriver = "/usr/lib/chromium-browser/chromedriver"
    driver = webdriver.Chrome(executable_path=chromedriver, options=options)
    print ('Browser started successfully. Navigating to the demo page to login.')
    driver.get('https://www.saucedemo.com/')
    driver.find_element("id",'user-name').send_keys(user)
    driver.find_element("id",'password').send_keys(password)
    driver.find_element("id",'login-button').click()
    print ('Login successfully')

    print ('Choose all items')
    items = driver.find_elements("class name",'inventory_item')
    for item in items:
        name = item.find_element("class name",'inventory_item_name')
        print ('Add ' + name.text + ' to cart')
        item.find_element("class name",'btn_inventory').click()
    
    print ('Go to cart')
    driver.find_element("class name",'shopping_cart_link').click()
    removes = driver.find_elements("class name", "cart_item")
    for remove in removes:
        name = remove.find_element("class name",'inventory_item_name')
        print ('Remove ' + name.text + ' from cart')
        remove.find_element("class name",'cart_button').click()

    print ('Done')

login('standard_user', 'secret_sauce')