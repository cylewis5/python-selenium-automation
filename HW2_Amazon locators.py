from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# get the path to the ChromeDriver executable
driver_path = ChromeDriverManager().install()

# create a new Chrome browser instance
service = Service(driver_path)
driver = webdriver.Chrome(service=service)
driver.maximize_window()

try:
    # Open Amazon's Sign-In page
    driver.get("https://www.amazon.com/")

    # 1. Amazon Logo - Clicking the logo will take you to the homepage
    amazon_logo = driver.find_element(By.XPATH, "//a[@aria-label='Amazon']")
    amazon_logo.click()
    sleep(2)  # Wait for the homepage to load

    # Go back to the Sign-In page
    driver.get("https://www.amazon.com/ap/signin")

    # 2. Email Field - Enter email
    email_field = driver.find_element(By.NAME, "email")
    email_field.send_keys("youremail@example.com")

    # 3. Continue Button - Click continue after entering email
    continue_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'].a-button-input")
    continue_button.click()
    sleep(2)

    # 4. Conditions of Use - Click the Conditions of Use link
    conditions_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Conditions of Use')]")
    conditions_link.click()
    sleep(2)

    # Go back to the Sign-In page
    driver.get("https://www.amazon.com/ap/signin")

    # 5. Privacy Notice - Click the Privacy Notice link
    privacy_notice_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Privacy Notice')]")
    privacy_notice_link.click()
    sleep(2)

    # Go back to the Sign-In page
    driver.get("https://www.amazon.com/ap/signin")

    # 6. Need Help? - Click the Need Help? link
    need_help_link = driver.find_element(By.XPATH, "//span[contains(text(), 'Need help')]/..")
    need_help_link.click()

    sleep(2)

    # Go back to the Sign-In page
    driver.get("https://www.amazon.com/ap/signin")

    # 7. Forgot Your Password? - Click Forgot your password? link
    forgot_password_link = driver.find_element(By.XPATH, "//a[contains(text(), 'Forgot your password')]")
    forgot_password_link.click()

    sleep(2)

    # Go back to the Sign-In page
    driver.get("https://www.amazon.com/ap/signin")

    # 8. Other Issues with Sign-In - Click Other issues with Sign-In link
    other_issues_link = driver.find_element(By.XPATH, "//a[text()='Other issues with Sign-In']")
    other_issues_link.click()

    sleep(2)

    # Go back to the Sign-In page
    driver.get("https://www.amazon.com/ap/signin")

    # 9. Create Your Amazon Account - Click the Create Account button
    create_account_button = driver.find_element(By.CLASS_NAME, "a#createAccountSubmit")
    create_account_button.click()
    sleep(2)

finally:
    # Close the driver after completion
    driver.quit()
