from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

path = "C:\\Users\jason\Documents\GitHub\Manga-Scraper\chromedriver.exe"
driver = webdriver.Chrome(path)

#set language setttings to english
driver.get("https://mangadex.org/settings")
click = driver.find_element_by_xpath("//*[@id='langs']/div/div[2]/div[2]")
click.click()
click = driver.find_element_by_xpath("//*[@id='langs']/div/div[2]/div[2]/div/div[2]/div[5]")
click.click()


#search for manga
driver.get("https://mangadex.org/titles")
print(driver.title)
#Go to search bar in advanced search
search = driver.find_elements_by_name("q")[1]

search.send_keys("hello")
search.send_keys(Keys.RETURN)

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "//*[@id='__layout']/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/a"))
    )
    
    for a in driver.find_elements_by_xpath("//*[@id='__layout']/div/div[2]/div[2]/div/div[2]/div[3]/div[1]/a"):
        link = a.get_attribute('href')
    
    driver.get(link)
    time.sleep(10)
finally:
    driver.quit()
