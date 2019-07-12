from selenium import webdriver

driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("")
driver.find_element_by_id('Email').clear()
driver.find_element_by_id('Email').send_keys('')
driver.find_element_by_id('Password').clear()
driver.find_element_by_id('Password').send_keys('')


def login():
    driver.find_element_by_xpath("//button[@class='login100-form-btn']").click()
    driver.implicitly_wait(20)
    print(driver.title)
    if driver.title.__contains__('My Profile'):
        print('Login Successfully')
    else:
        print('failed')
    print(driver.current_url)


login()


def logout():
    driver.find_element_by_xpath("//a[contains(text(),'Sign Out')]").click()
    print(driver.title)
    if driver.title.__contains__('Home'):
        print('Log Out Successfully')
    else:
        print('Not Working')
    print(driver.current_url)


logout()
driver.quit()
