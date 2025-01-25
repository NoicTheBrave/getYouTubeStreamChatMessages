from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

def is_livestreaming(channel_url):
    # Configure Selenium WebDriver
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Run in headless mode for efficiency
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    
    try:
        # Initialize WebDriver (ChromeDriver is assumed to be in PATH)
        driver = webdriver.Chrome(options=chrome_options)
        
        # Open the channel URL
        driver.get(channel_url)
        time.sleep(3)  # Allow time for dynamic content to load
        
        # Look for aria-label indicating a live stream
        try:
            live_element = driver.find_element(By.CSS_SELECTOR, '[aria-label="Tap to watch live"]')
            return True
        except Exception:
            pass  # If the element is not found, we ignore the error
        
        # Look for live badge text
        try:
            live_badge = driver.find_element(By.CSS_SELECTOR, '.yt-spec-avatar-shape__badge-text')
            if live_badge.text.strip().upper() == "LIVE":
                return True
        except Exception:
            pass  # If the element is not found, we ignore the error
        
        return False  # No live indicators found
    except Exception as e:
        print(f"An error occurred: {e}")
        return False
    finally:
        # Ensure the WebDriver is closed
        driver.quit()

# Example usage
#channel_url = "https://www.youtube.com/@noicthebrave"
channel_url = "https://www.youtube.com/@PirateSoftware"
if is_livestreaming(channel_url):
    print("The channel is currently livestreaming.")
else:
    print("The channel is not livestreaming.")
