import time
from selenium import webdriver
from getpass import getpass
browser = webdriver.Edge(r"<PATH TO DRIVER (EXE) >")     #for MS Edge browser
# browser = webdriver.Chrome(r"<PATH TO DRIVER (EXE) >") #for chrome broswer
browser.get('https://www.codechef.com/login?destination=/')
time.sleep(5)
username_element = browser.find_elements_by_id('edit-name')[2]
username_element.clear()       #clears the field
username_element.send_keys(input("Enter User id:  "))
password_element = browser.find_elements_by_id('edit-pass')[1]
password_element.clear()  
password_element.send_keys(getpass("Enter Password:  "))
browser.find_elements_by_id('edit-submit-button')[1].click()
time.sleep(3)
question_id  = input('Enter Question ID:  ')
browser.get('https://www.codechef.com/submit/{}'.format(question_id))
time.sleep(3)
if(browser.find_elements_by_id("edit_area_toggle_checkbox_edit-program") == [] ):
    switch_text = browser.find_elements_by_id('edit-submit')[0]
    switch_text.click()
code_element=browser.find_element_by_id('edit-program')
if code_element.is_displayed()==False:
    browser.find_element_by_id('edit_area_toggle_checkbox_edit-program').click()
code_element=browser.find_element_by_id('edit-program')
with open('<PATH_TO_FILE>','r') as f:
    code = f.read()
code_element.clear()
code_element.send_keys(code)
select_language_element = browser.find_element_by_xpath('//*[@id="edit-language"]/option[1]').click()
submit_button_element = browser.find_element_by_id('edit-submit-1').click()