from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

driver = webdriver.Chrome(ChromeDriverManager().install())
driver.maximize_window()
driver.get("https://www.google.com")
print("Title of this link is: ", driver.title)
print("Title of this url is: ", driver.current_url)
