from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import pandas as pd

options = webdriver.ChromeOptions()
driver = webdriver.Chrome(options=options)

# Define the base URL
base_url = "https://poets.org/poems?page={}"

# Initialize an empty list to store poem data
poem_data = []

# Iterate over each page
for page_num in range(751):
    url = base_url.format(page_num)
    print("Scraping page", page_num + 1)
    driver.get(url)
    
    try:
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "tbody tr")))
    except TimeoutException:
        print("Timeout waiting for poem elements to load on page", page_num + 1)
        continue

    # Scrape poem names and links
    poem_elements = driver.find_elements(By.CSS_SELECTOR, "tbody tr")
    for poem_element in poem_elements:
        poem_name_element = poem_element.find_element(By.TAG_NAME, "a")
        poem_name = poem_name_element.text.strip()
        poem_link = poem_name_element.get_attribute("href")
        poem_data.append({'Poem Name': poem_name, 'Poem Link': poem_link})

# Convert data to a pandas DataFrame
poems_df = pd.DataFrame(poem_data)

# Save the DataFrame to a CSV file
poems_df.to_csv("poems_links_all_pages.csv", index=False)

# Close the browser
driver.quit()
