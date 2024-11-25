from pathlib import Path

import httpx

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


url = "https://www.zillow.com/homedetails/"
url += "432-Park-Ave-PENTHOUSE-New-York-NY-10022/2069500049_zpid/"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

# Open main property page.
driver.get(url)

# Click on first image in listing.
button = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((
        By.CSS_SELECTOR,
        "button[aria-label='view larger view of the 1 photo of this home']"
    ))
)
button.click()

breakpoint()
