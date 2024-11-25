from pathlib import Path

import httpx

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


url = "https://www.zillow.com/homedetails/"
url += "432-Park-Ave-PENTHOUSE-New-York-NY-10022/2069500049_zpid/"

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()))

# Open main property page.
driver.get(url)

breakpoint()
