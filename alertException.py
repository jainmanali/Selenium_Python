from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as cond
from selenium.common.exceptions import NoAlertPresentException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import InvalidSelectorException
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.seleniumeasy.com/test/javascript-alert-box-demo.html")

driver.find_element_by_xpath("//button[@class='btn btn-default']").click()
try:
    WebDriverWait(driver, 50).until(cond.alert_is_present())
    alert_window = driver.switch_to.alert
    msg = alert_window.text
    print(msg)
    alert_window.accept()
except (NoAlertPresentException, TimeoutException) as alert_ex:
    print(alert_ex)
    print(alert_ex.args)
try:
    driver.find_element_by_xpath("//button[@class='btn btn-default btn-lg'][contains(text(),'Click me!'").click()
    WebDriverWait(driver, 10).until(cond.alert_is_present())
    alert_box = driver.switch_to.alert
    txt = alert_box.text
    print(txt)
    alert_window.accept()
except (InvalidSelectorException, NoSuchElementException) as ex:
    print(ex)
    print(ex.args)
finally:
    driver.quit()



