from selenium import webdriver
from selenium.webdriver.common.by import By

# Create a new instance of the Firefox driver (you can use other drivers like Chrome as well)
driver = webdriver.Chrome()

# Navigate to the website
driver.get("https://lowcars.co.in")

try:
    # Find and click the login button
    login_button = driver.find_element(By.LINK_TEXT, "Contact")
    login_button.click()

    # Wait for a few seconds to allow the page to load after clicking the button
    driver.implicitly_wait(5)  # You can adjust the waiting time as needed
    login_button = driver.find_element(By.LINK_TEXT, "Offers")
    driver.implicitly_wait(5)
    login_button.click()
    # Print the current page's HTML content
    print(driver.page_source)

except Exception as e:
    print("An error occurred:", e)

# Close the browser
# driver.quit()
