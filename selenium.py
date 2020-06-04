from selenium import webdriver

driver = webdriver.chrome()
driver.get('http://url.com')
search = driver.find_element_by_xpath('xpath from inspect')

search.send_keys('query')

enter = driver.find_element_by_xpath('xpath for enter button')
enter.click()
