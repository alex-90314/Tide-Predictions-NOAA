'''
guide for using selenium to search the web
https://towardsdatascience.com/controlling-the-web-with-python-6fceb22c5f08

API call that creates the .CSV file and auto downloads it
https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?date=latest&station=8723214&product=predictions&datum=MLW&time_zone=lst&units=english&format=csv
'''
from selenium import webdriver

driver = webdriver.Chrome()

station_ID = 8723214
website = (f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?date=latest&station={station_ID}&product=predictions&datum=MLLW&time_zone=lst&units=english&format=csv")

driver.get(website)