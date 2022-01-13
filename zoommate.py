from selenium import webdriver
from datetime import datetime

start_time = datetime.now()


browser = webdriver.Chrome(executable_path="chromedriver")

browser.get('http://lms.fsm.edu.tr/login/ogrenci')

email= browser.find_element_by_id('username') 
email.send_keys('yunusemre.adas')

password= browser.find_element_by_id('password') 
password.send_keys('Yu11288329554**')

password.submit()


element = browser.find_elements_by_xpath("//div[@class = 'event']/a")
element[0].click()

time.sleep(3)


#browser.find_element_by_class_name('event').click()
#browser.find_element_by_css_selector(".event:firstchild[data-region='event-item']").click()
#https://fsm-edu-tr.zoom.us/j/91380464854?pwd=QnppbmlSbERYb3MwMjFNOVRVNDU5dz09 - sayısal sistemler

