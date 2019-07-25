from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


def click_hold():
    driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.amazon.in/")
    element = driver.find_element_by_xpath("//a[@id='nav-link-accountList']//span[@class='nav-icon nav-arrow'] ")
    ActionChains(driver).click_and_hold(element).perform()
    driver.implicitly_wait(500)
    driver.quit()


def right_click():
    driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
    actionchain = ActionChains(driver)
    element = driver.find_element_by_xpath("//span[@class='context-menu-one btn btn-neutral']")
    actionchain.context_click(element).perform()
    driver.quit()


def double_click():
    driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
    driver.maximize_window()
    driver.delete_all_cookies()
    driver.get("https://www.w3schools.com/jsref/tryit.asp?filename=tryjsref_ondblclick")
    element = driver.find_element_by_css_selector("body > div")
    # Scroll down the page
    ActionChains(driver).move_to_element(element).perform()
    ActionChains(driver).double_click(element).perform()
    driver.implicitly_wait(80)


# click_hold()
# right_click()
double_click()
