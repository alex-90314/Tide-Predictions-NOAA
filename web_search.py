import selenium

driver = webdriver.Chrome()

station_ID = 8723214
website = (f"https://api.tidesandcurrents.noaa.gov/api/prod/datagetter?date=latest&station={station_ID}&product=predictions&datum=MLLW&time_zone=lst&units=english&format=csv")

driver.get(website)