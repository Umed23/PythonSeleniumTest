import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

@pytest.mark.parametrize("query", ["OpenAI", "Python", "Selenium"])
def test_google_search(query):
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys(query, Keys.RETURN)
    assert query in driver.title
    driver.quit()
