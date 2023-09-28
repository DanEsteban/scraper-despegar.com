from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import time

# Inicializa el controlador de Chrome
driver = webdriver.Firefox()
driver.get("https://www.reddit.com/")

try:
    login_button = driver.find_element(by=By.CSS_SELECTOR, value="#login-button")
    login_button.click()

    # Wait for the login form to be displayed
    wait = WebDriverWait(driver, 10)
    wait.until(lambda driver: driver.find_element(by=By.ID, value='loginUsername').is_displayed())

    # Wait for the username input field to be available
    wait.until(lambda driver: driver.find_element(by=By.ID, value='loginUsername').is_enabled())

    username_input = driver.find_element(by=By.ID, value='loginUsername')
    username_input.send_keys('swing772')

    password_input = driver.find_element(by=By.ID, value="loginPassword")
    password_input.send_keys('ciberseguridad.28')

    driver.close()

except Exception as e:
    print("Ocurrió un error:", e)
    driver.quit()
