from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


import time

def elementWait(xPATH, driver, time):
    element = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.XPATH, xPATH)))
        
def scrape(id):
    url = 'https://www.ubisoft.com/en-us/game/rainbow-six/siege/marketplace?route=buy%2Fitem-details&itemId=' + id
    driver.get(url)
    elementWait('/html/body/div[1]/div[5]/div/div/ubisoft-connect', driver, 60)

    shadow_root = driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div/div/ubisoft-connect').shadow_root
    shadow_host = shadow_root.find_element(by= By.CSS_SELECTOR, value = 'iframe:nth-child(2)')
    driver.switch_to.frame(shadow_host)

    last_sold_at_xPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[1]/span[2]/div/div/div[2]/span'
    elementWait(last_sold_at_xPATH, driver, 60)
    last_sold_at_scrape = driver.find_element(by=By.XPATH, value= last_sold_at_xPATH)
    last_sold_at = last_sold_at_scrape.text
 
    price_range_xPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[2]/span[2]/div/div/div[2]/span'
    elementWait(price_range_xPATH, driver, 60)
    price_range_scrape = driver.find_element(by=By.XPATH, value=price_range_xPATH)
    price_range_min = price_range_scrape.text.split()[0]
    price_range_max = price_range_scrape.text.split()[2]

    sale_orders_xPATH = '/html/body/div[2]/div/div/div[1]/div[1]/div[2]/div/div/div[4]/div[1]/div/div/div[2]/div/div[2]/div[2]/div[2]/div[3]'
    elementWait(sale_orders_xPATH, driver, 60)
    sale_orders_scrape = driver.find_element(by=By.XPATH, value= sale_orders_xPATH)
    sale_orders = sale_orders_scrape.text.splitlines()[1]

    #print('no error')

    return last_sold_at, price_range_min, price_range_max, sale_orders

    


# Path to the downloaded ChromeDriver executable
PATH = "chromedriver.exe"

# Create a Chrome browser instance
service = Service(executable_path= PATH)
driver = webdriver.Chrome(service= service)

# Navigate to a website
driver.get('https://www.ubisoft.com/en-us/game/rainbow-six/siege/marketplace?route=buy')

elementWait('/html/body/div[1]/div[5]/div/div/div[1]/div/div/div[2]/button', driver, 10)

driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div/div/div[1]/div/div/div[2]/button').click()
driver.find_element(by=By.XPATH, value='/html/body/div[1]/div[5]/div/div/div[1]/div/div/div[2]/button').click()

time.sleep(5)

currHand = driver.current_window_handle

handles = driver.window_handles


for handle in handles:
    driver.switch_to.window(handle)
    if(currHand != handle):
        driver.find_element(by=By.XPATH, value='//*[@id="AuthEmail"]').send_keys("Cabello.9@osu.edu")
        driver.find_element(by=By.XPATH, value='//*[@id="AuthPassword"]').send_keys("Fifth5Account*")
        driver.find_element(by=By.XPATH, value='/html/body/app-component/div/app-login-component/main/app-login-shared-component/section/form/button').click()
    
    driver.switch_to.window(currHand)







