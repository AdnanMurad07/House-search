import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver_url = "https://forms.gle/3Nt3t2qvut3z2a3W7"

url = "https://appbrewery.github.io/Zillow-Clone/"
response = requests.get(url=url)
content = response.text

soup = BeautifulSoup(content, "html.parser")
prices = soup.find_all(name="span", class_="PropertyCardWrapper__StyledPriceLine")
prices_list = [price.text for price in prices]
# print(prices_list)
addresses = soup.find_all(name="address")
addresses_list = [address.text for address in addresses]
# print(addresses_list[0].lstrip())
links = soup.find_all(name="a",class_="StyledPropertyCardDataArea-anchor", href=True)
links_list = [link["href"] for link in links]
# print(links_list)

for i in range(39, 44):
    driver = webdriver.Chrome(options=chrome_options)
    driver.get(driver_url)
    time.sleep(5)
    address_bar = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    rent_bar = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link_bar = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    time.sleep(2)
    address_bar.send_keys(addresses_list[i].lstrip())
    time.sleep(2)
    rent_bar.send_keys(prices_list[i])
    time.sleep(2)
    link_bar.send_keys(links_list[i])
    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, value="//*[text()='Submit']")
    submit_button.click()
    driver.quit()

