from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
import pandas as pd

# Set up Chrome driver
options = webdriver.ChromeOptions()
options.headless = True  # Run in headless mode to hide browser window
driver = webdriver.Chrome(options=options)

# Read poem names and links from the pandas DataFrame
poem_links_df = pd.read_csv("split_dataset_15.csv")

# Create empty lists to store poem data
poem_names = []
poem_contents = []

# Iterate through each row of the DataFrame
for index, row in poem_links_df.iterrows():
    poem_name = row["Poem Name"]
    poem_link = row["Poem Link"]
    
    try:
        driver.get(poem_link)
        print("colleceting poem: ",index)
        
        # Find poem content
        poem_content = driver.find_element(By.CLASS_NAME, "field--body").text

        # Append to lists
        poem_names.append(poem_name)
        poem_contents.append(poem_content)
        
    except WebDriverException as e:
        print(f"Error scraping poem '{poem_name}': {str(e)}")
        continue

# Close the browser
driver.quit()

# Create DataFrame
df = pd.DataFrame({
    "Poem Name": poem_names,
    "Poem Content": poem_contents
})

# Save DataFrame to CSV
df.to_csv("poem_data15.csv", index=False)
