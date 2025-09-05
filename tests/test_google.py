import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@pytest.mark.parametrize("query", ["OpenAI", "Python", "Selenium"])
def test_google_search(query):
    # Set Chrome options for headless mode (CI friendly)
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com")
    
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query, Keys.RETURN)
    
    # Wait up to 10 seconds until the title contains the search query
    WebDriverWait(driver, 10).until(EC.title_contains(query))
    
    assert query in driver.title
    driver.quit()
