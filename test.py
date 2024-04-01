from selenium import webdriver
import time

# Using Chrome to access web
driver = webdriver.Chrome()
# Open the website
driver.get('https://www.example.com')
time.sleep(5)
