from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def get_live_stream_url(channel_url):
    # Set up the Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Run in headless mode (no UI)
    
    # Create a new instance of Chrome WebDriver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Navigate to the YouTube channel
    driver.get(channel_url)
    
    # Wait for dynamic content to load (using a reasonable wait time)
    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "ytd-item-section-renderer"))
    )
    
    try:
        # Now, wait for the element with 'aria-label="Tap to watch live"' to appear
        live_video_element = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(@aria-label, 'Tap to watch live')]"))
        )
        
        # Extract the live stream URL
        live_url = live_video_element.get_attribute("href")
        return live_url
    except Exception as e:
        # For debugging, let's print the page source to understand the issue
        print("Error occurred:", str(e))
        print("Page source:", driver.page_source)  # This prints the page's HTML for debugging
        return "No live stream found or an error occurred."
    finally:
        driver.quit()

# Example usage
channel_url = "https://www.youtube.com/@PirateSoftware"
live_stream_url = get_live_stream_url(channel_url)
print("Live stream URL:", live_stream_url)
