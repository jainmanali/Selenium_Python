from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.in/")

# implicit wait
driver.implicitly_wait(40)
driver.find_element_by_xpath("//span[contains(text(),'Hello, Sign in')]").click()

# Conditions
# Element enabled or not condition (is_enabled)
txtbox_email = driver.find_element_by_id('ap_email')
if txtbox_email.is_enabled():
    txtbox_email.send_keys('jmanali4096@gmail.com')
    print('Element is enabled')
# Element is displayed or not condition (is_Displayed)
nxt_button = driver.find_element_by_id('continue')
while (nxt_button.is_displayed()):
    driver.find_element_by_id('continue').click()
    print('Element is displayed')
    driver.find_element_by_id('ap_password').send_keys('manali123')
    driver.find_element_by_id('signInSubmit').click()
    break
# Radio button, check box or drop down is selected or not (is_Selected)
driver.find_element_by_id('searchDropdownBox').click()
d = Select(driver.find_element_by_id('searchDropdownBox'))
d.select_by_value('search-alias=amazon-devices')
if driver.find_element_by_id('searchDropdownBox').is_selected():
    print('Element is selected')
    driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('Alexa')
    driver.find_element_by_class_name('nav-input').click()

# Explicit Wait
# Wait until element is visible
wait = WebDriverWait(driver, 20)
txt = wait.until(EC.element_to_be_clickable((By.ID, 'nav-your-amazon-text')))
driver.find_element_by_id('nav-your-amazon-text').click()



