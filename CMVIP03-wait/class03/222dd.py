from selenium import webdriver

driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)
driver.get('http://39.98.138.157/shopxo/index.php?s=/index/user/reginfo.html')
driver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[2]/div/div/div[1]/form/div[3]/label').click()