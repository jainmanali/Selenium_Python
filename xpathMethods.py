from selenium import webdriver

driver = webdriver.Chrome("C:\\Chrome\\chromedriver.exe")
driver.maxixmize_window()
driver.delete_all_cookies()
driver.get("http://demo.guru99.com/v1/")

# XPath Methods

# Contain Method
driver.find_element_by_xpath("//*[contains (@type,'sub')]")
# Or Method
driver.find_element_by_xpath("//*[@name='btn' or @type='submit']")
# And Method
driver.find_element_by_xpath("//*[@name='btnLogin' and @type='submit']")
# Start-with Method
driver.find_element_by_xpath("//label[starts-with(@id, 'message')]")
# Text Method
driver.find_element_by_xpath("//td[text() = 'UserID']")
# Following Method
driver.find_element_by_xpath("//*[@type='text'] //following::input[1]")
# Ancestor Method
driver.find_element_by_xpath("//*[text()='Enterprise Testing']//ancestor::div[1]")
# Child Method
driver.find_element_by_xpath("//*[@id='java_technologies']/child::li[1]")
# Preceding Method
driver.find_element_by_xpath("//*[@type='submit']//preceding::input[1]")
# Following Sibling Method
driver.find_element_by_xpath("//*[@type='submit']//following-sibling::input")
# Parent Method
driver.find_element_by_xpath("//*[@id='rt-feature']//parent::div[1]")
# Self Method
driver.find_element_by_xpath("//*[@type='password']//self::input")
# Descendant Method
driver.find_element_by_xpath("//*[@id='rt-feature']//descendant::a[1]")
# select element in table by width
driver.find_element_by_xpath("//table[@width=\"270\"]/tbody/tr[4]/td")
# method to go to next row in table
# No of rows
col = []
col = driver.find_element_by_xpath(".//*[@id='leftcontainer']/table/thead/tr/th")
# No of columns
rows = []
rows = driver.find_element_by_xpath(".//*[@id='leftcontainer']/table/tbody/tr/td[1]")
for i in range(2,rows.size):
    max = driver.find_element_by_xpath("html/body/div[1]/div[5]/table/tbody/tr[" + (i+1) + "]/td[4]").text
