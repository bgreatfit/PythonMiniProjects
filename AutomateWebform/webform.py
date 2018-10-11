from selenium import webdriver

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://canvas.case.edu')

#select id box
id_box = driver.find_element_by_name('username')
#select password box
password_box = driver.find_element_by_name('password')
#send key information
id_box.send_keys('my_username')
password_box.send_keys('my_password')

#find submit button
submit_button = driver.find_element_by_name('submit')
submit_button.click()
# seq = ['a','b','c']
# 'abc'.join()