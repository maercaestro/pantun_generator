import requests
from bs4 import BeautifulSoup
import time
from tqdm import tqdm

# Base URL of the page to scrape
base_url = "https://malaycivilization.com.my/items/browse?collection=10&page={}"

# Create a session to manage cookies and headers
session = requests.Session()
session.headers.update({
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
})

# Open a file to save the scraped pantuns
with open('pantun_dataset3.txt', 'a', encoding='utf-8') as f:
    # Iterate over pages, for example from page 1 to 5 (update as necessary)
    for page_number in tqdm(range(1, 5298), desc="Scraping pages"):
        # Format the URL for the specific page
        url = base_url.format(page_number)
        
        # Request the HTML content of the page
        response = session.get(url)
        if response.status_code == 200:
            # Parse the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Find all h2 elements that contain the pantun text
            h2_elements = soup.find_all('h2')

            # Iterate over each h2 element to extract pantun text
            for h2 in h2_elements:
                a_tag = h2.find('a')
                if a_tag:
                    # Get the text and replace line breaks with newline characters
                    pantun = a_tag.get_text(separator="\n").strip()
                    
                    # Write the pantun to the file
                    f.write(pantun + '\n\n')
        else:
            print(f"Failed to retrieve content from page {page_number}. Status code: {response.status_code}")
        
        # Add a delay to prevent overwhelming the server
        time.sleep(1)

print("Scraping and saving completed.")