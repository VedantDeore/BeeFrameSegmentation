import urllib.request
import os
import time
from tqdm import tqdm
import logging
from urllib.error import URLError, HTTPError
from socket import timeout

# Configuration options
URLS_PATH = "images_urls.csv"  # Path to the CSV file with URLs
OUTPUT_PATH = "BEE_original_images"  # Directory to save the downloaded images
DELAY_BETWEEN_REQUESTS = 5  # Delay between each request in seconds
RETRIES = 3  # Number of retries for failed downloads

# Create the output directory if it doesn't exist
if not os.path.exists(OUTPUT_PATH):
    os.makedirs(OUTPUT_PATH)

# Setup logging
logging.basicConfig(
    filename="download_log.txt",
    level=logging.INFO,
    format="%(asctime)s:%(levelname)s:%(message)s"
)

# Function to validate URLs
def is_valid_url(url):
    """Check if a URL is valid."""
    try:
        urllib.request.urlopen(url, timeout=5)
        return True
    except (HTTPError, URLError, timeout):
        return False

# Function to download an image
def download_image(url, file_path):
    """Download an image from a URL and save it to a file path."""
    for attempt in range(RETRIES):
        try:
            urllib.request.urlretrieve(url, file_path)
            logging.info(f"Downloaded: {file_path}")
            print(f"Downloaded: {file_path}")
            return True
        except (HTTPError, URLError, timeout) as e:
            logging.error(f"Failed to download {url} on attempt {attempt + 1}. Error: {e}")
            print(f"Failed to download {url} on attempt {attempt + 1}. Error: {e}")
            time.sleep(DELAY_BETWEEN_REQUESTS)  # Wait before retrying
    return False

# Read the CSV file and process the URLs
with open(URLS_PATH, "r") as file:
    urls = [line.strip().split(",") for line in file.readlines()]

# Download each image if it doesn't already exist
for filename, url in tqdm(urls, desc="Downloading images", unit="image"):
    file_path = os.path.join(OUTPUT_PATH, filename)
    if not os.path.exists(file_path):
        if is_valid_url(url):
            if not download_image(url, file_path):
                logging.warning(f"Giving up on {url} after {RETRIES} attempts.")
        else:
            logging.error(f"Invalid URL: {url}")
            print(f"Invalid URL: {url}")
    else:
        print(f"Already exists: {filename}")
        logging.info(f"Already exists: {file_path}")

print("All images have been downloaded or were already present.")


# import urllib.request
# import os
# from tqdm import tqdm

# # Define paths and settings
# URLS_PATH = "images_urls.csv"  # Path to the CSV file with URLs
# OUTPUT_PATH = "BEE_original_images"  # Directory to save the downloaded images
# DELAY_BETWEEN_REQUESTS = 5  # Delay between each request in seconds

# # Create the output directory if it doesn't exist
# if not os.path.exists(OUTPUT_PATH):
#     os.makedirs(OUTPUT_PATH)

# # Read the CSV file and process the URLs
# with open(URLS_PATH, "r") as file:
#     urls = [i.strip().split(",") for i in file.readlines()]

# # Download each image if it doesn't already exist
# for filename, url in tqdm(urls):
#     file_path = os.path.join(OUTPUT_PATH, filename)
#     if not os.path.exists(file_path):
#         try:
#             # Download the image and save it with the original filename
#             urllib.request.urlretrieve(url, file_path)
#             print(f"Downloaded: {filename}")
#         except Exception as e:
#             print(f"Failed to download {filename}. Error: {e}")
        
#         # Optional: Wait before the next request to prevent server overload
#         # time.sleep(DELAY_BETWEEN_REQUESTS)
#     else:
#         print(f"Already exists: {filename}")

# print("All images have been downloaded or were already present.")
