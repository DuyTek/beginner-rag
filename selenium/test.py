from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Create a new instance of the Chrome driver
driver = webdriver.Chrome()

try:
    # Open a website
    driver.get("https://www.google.com")
    
    # Find the search box element by name attribute
    search_box = driver.find_element(By.NAME, "q")
    
    # Type in the search box
    search_box.send_keys("Selenium automation")
    
    # Submit the form
    search_box.send_keys(Keys.RETURN)
    
    # Wait for the results to load
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "search"))
    )
    
    # Print the title of the page
    print("Page title:", driver.title)
    
    # Verify that "Selenium" is in the title
    assert "Selenium" in driver.title, "Selenium not in title"
    
    # Get search results
    results = driver.find_elements(By.CSS_SELECTOR, "div.g")
    print(f"Found {len(results)} search results")
    
    # Wait a moment to see the results
    time.sleep(3)
    
    print("Test completed successfully!")
    
except Exception as e:
    print(f"Test failed: {e}")
    
finally:
    # Close the browser
    driver.quit()