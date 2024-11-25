from pathlib import Path
from random import randint
from time import sleep
import re

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

# On main photos page. Click first image button.
li_element = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR, "li.viw-tile-0"))
)
button = li_element.find_element(
    By.CSS_SELECTOR, "button[data-cy='loaded-photo-tile']")
button.click()

# On single photo page. Find out how many photos.
carousel_counter = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((
        By.CSS_SELECTOR,
        "div[class*='GalleryLightboxResponsiveImage__StyledCarouselCounter']"))
)
counter_text = carousel_counter.get_attribute("innerHTML")
of_index = counter_text.find("of")
num_images = int(counter_text[of_index+3:])

# Click through and download all images.
for img_num in range(num_images):

    # On a single photo page. Find div containing image.
    div_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((
            By.CSS_SELECTOR, "div.hdp-photo-gallery-lightbox-content"))
    )

    # Extract image source URL.
    img_re = r'img src="(https://photos\.zillowstatic\.com/fp/.*?uncropped_scaled_within.*?\.jpg)'
    div_html = div_element.get_attribute("innerHTML")
    m = re.search(img_re, div_html)
    if m:
        img_url = m.groups()[0]

        # Get image, write image to file.
        r = httpx.get(img_url)
        path = (
            Path(__file__).parent
            / "output_images"
            / f"property_image_{img_num}.jpg"
        )
        path.write_bytes(r.content)
    else:
        print("Could not find image URL.")

    # Pause 1-3 seconds.
    wait_time = randint(1000, 3000) / 1000
    sleep(wait_time)

    # Click to next picture.
    next_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "li.photo-carousel-right-arrow button"))
    )
    next_button.click()

    # Pause 1-3 seconds.
    wait_time = randint(1000, 3000) / 1000
    sleep(wait_time)

breakpoint()
