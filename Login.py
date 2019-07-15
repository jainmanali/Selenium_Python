from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
# Redirect to amazon home page
driver.get("https://www.amazon.in/")
# get title
title = driver.title


def loginmethod():

    driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in')]").click()
    driver.find_element_by_id('ap_email').send_keys('jmanali4096@gmail.com')
    driver.find_element_by_id('continue').click()
    driver.find_element_by_id('ap_password').send_keys('manali123')
    driver.find_element_by_id('signInSubmit').click()
    # catch user name
    text = driver.find_element_by_xpath('//*[@id="nav-link-accountList"]/span[1]').text
    if text.__contains__('Manali'):
        print('Login Successfully')
    else:
        print('Not login Successfully')


def logoutmethod():
    element_hover = driver.find_element_by_id('nav-link-accountList')
    hover = ActionChains(driver).move_to_element(element_hover)
    hover.perform()
    driver.implicitly_wait(50)
    driver.find_element_by_xpath("//span[contains(text(),'Sign Out')]").click()
    driver.implicitly_wait(50)
    title1 = driver.title
    if title1.__eq__('Amazon Sign In'):
        print('Log Out Successfully')
    else:
        print('Log Out not working')


if title.__contains__('Online Shopping site in India'):
    print('Redirect to amazon site')
    # Login Method
    loginmethod()
    # Logout Method
    logoutmethod()
    driver.quit()
else:
    print('Not redirect to amazon site')

