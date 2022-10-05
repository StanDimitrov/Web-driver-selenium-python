from lib2to3.pgen2 import driver
from selenium import webdriver

PATH = "C:\Program Files\Python310\chromedriver.exe"
driver = webdriver.Chrome(PATH)

web = driver.get("https://www.google.com/")
validate_web = driver.find_element(By.ID, "L2AGLb")
validate_web.click()

# Check to see if the search results are showing up
driver.find_element(By.NAME, "q").send_keys("Alphabet share price" + Keys.ENTER)