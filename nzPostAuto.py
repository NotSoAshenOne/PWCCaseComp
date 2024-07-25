# from selenium import webdriver
# from selenium.webdriver.firefox.options import Options
# import time

# options = Options()
# driver = webdriver.Firefox(options=options)

# driver.get("https://www.nzpost.co.nz/tools/rate-finder/sending-nz/parcels")

# time.sleep(20)

# nxt = driver.find_element_by_xpath("//*[@id='edit-next']")
# nxt.click()

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select

# Configure Firefox options
options = webdriver.FirefoxOptions()
options.headless = False  # Set to True if running headless

# Initialize WebDriver
driver = webdriver.Firefox(options=options)

# try:
#     # Open the webpage
#     driver.get("https://www.nzpost.co.nz/tools/rate-finder/sending-nz/parcels")

#     # Wait for the button to be clickable
#     nxt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#edit-next")))

#     # Click the button
#     nxt.click()

#     # Optional: Wait for some time to see the effect or continue interacting with the next page
#     driver.implicitly_wait(10)  # Example implicit wait

# finally:
#     # Close the WebDriver session
#     # driver.quit()
#     x =0 


# Open the webpage
driver.get("https://www.nzpost.co.nz/tools/rate-finder/sending-nz/parcels")

address1 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#edit-sender-addr")))
address1.send_keys("36 Mary Carpenter Avenue, Yaldhurst, Christchurch 8042")
address2 = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#edit-destination-addr")))
address2.send_keys("7A Delaware Crescent, Russley, Christchurch 8042")
# Wait for the button to be clickable
nxt = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#edit-next")))

# Click the button
nxt.click()
# Optional: Wait for some time to see the effect or continue interacting with the next page
# Example implicit wait

#driver.get("https://www.nzpost.co.nz/tools/rate-finder/sending-nz/parcels")
WebDriverWait(driver, 20).until(EC.url_changes(driver.current_url))


# box = driver.find_elements(by = By.ID, value = "edit-preset-dims")
box = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#edit-preset-dims")))
WebDriverWait(driver, 20).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#edit-preset-dims > option:nth-child(2)")))
Select(box).select_by_index(1)
#box[1].click()
driver.implicitly_wait(10)

