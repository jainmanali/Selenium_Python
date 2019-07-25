from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.maximize_window()
driver.delete_all_cookies()
driver.get("https://www.amazon.in/")
# method to check title
assert "Online" in driver.title
driver.find_element_by_id('searchDropdownBox').click()
# Methods to handle Drop down
# Using Value
d = Select(driver.find_element_by_id('searchDropdownBox'))
d.select_by_value('search-alias=amazon-devices')
# Using Visible Text
d1 = Select(driver.find_element_by_id('searchDropdownBox'))
d1.select_by_visible_text('Amazon Devices')
# Using Index
d2 = Select(driver.find_element_by_id('searchDropdownBox'))
d2.select_by_index(3)

# Insert values to search box
driver.find_element_by_xpath("//input[@id='twotabsearchtextbox']").send_keys('Alexa')
driver.find_element_by_class_name('nav-input').click()
driver.implicitly_wait(50)

# Sort Items
driver.find_element_by_id('a-autoid-0-announce').click()
driver.find_element_by_id('s-result-sort-select_1').click()
driver.implicitly_wait(50)

# Get price of all products
text = []
table = driver.find_element_by_xpath("//div[@class = 's-result-list s-search-results sg-row']")
no_of_item = table.find_elements_by_xpath("//span[@class='a-price-whole']")
for item in no_of_item:
    text.append(item.text)
print(text)






