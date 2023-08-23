import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

driver.get("http://secure-retreat-92358.herokuapp.com/")


first_name = driver.find_element(By.NAME, "fName")
first_name.send_keys("Gopi")

last_name = driver.find_element(By.NAME, "lName")
last_name.send_keys("Patel")

#dummy email
email = driver.find_element(By.NAME, "email")
email.send_keys("gopiPatel@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "button")
submit.click()

time.sleep(5)
