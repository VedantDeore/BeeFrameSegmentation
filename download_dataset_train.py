import urllib.request
import os
from tqdm import tqdm

# Define paths and settings
URLS_PATH = "images_urls.csv"  # Path to the CSV file with URLs
OUTPUT_PATH = "BEE_original_images"  # Directory to save the downloaded images
DELAY_BETWEEN_REQUESTS = 5  # Delay between each request in seconds

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

# Read the CSV file and process the URLs
with open(URLS_PATH, "r") as file:
    urls = [i.strip().split(",") for i in file.readlines()]

# Download each image if it doesn't already exist
for filename, url in tqdm(urls):
    file_path = os.path.join(OUTPUT_PATH, filename)
    if not os.path.exists(file_path):
        try:
            # Download the image and save it with the original filename
            urllib.request.urlretrieve(url, file_path)
            print(f"Downloaded: {filename}")
        except Exception as e:
            print(f"Failed to download {filename}. Error: {e}")
        
        # Optional: Wait before the next request to prevent server overload
        # time.sleep(DELAY_BETWEEN_REQUESTS)
    else:
        print(f"Already exists: {filename}")

print("All images have been downloaded or were already present.")
