from app.tools.sele import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time

# Specify the path to your driver
driver_path = "/Users/alexander/Downloads/ChromeDriver\ 114.0.5735.90/chromedriver"  # e.g., "C:/path/to/chromedriver"

# Create a new instance of the browser driver
driver = webdriver.Chrome(driver_path)

# Go to the webpage
driver.get("http://saia.ar")

# Wait for the page to load
time.sleep(5)

try:
    # Find the button and click it
    button = driver.find_element(
        By.ID, "button_id"
    )  # Replace "button_id" with the actual ID of the button
    button.click()

    # Additional actions can be performed here

except NoSuchElementException:
    print("Button not found")

finally:
    # Close the browser after a delay
    time.sleep(10)
    driver.quit()
