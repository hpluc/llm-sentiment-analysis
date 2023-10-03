import requests
from bs4 import BeautifulSoup

# Function to crawl a page and extract titles and links
def crawl_page(url):
    try:
        # Send an HTTP GET request to the URL
        response = requests.get(url)
        
        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the HTML content of the page using BeautifulSoup
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract titles and links
            titles = soup.find_all('h1')
            links = soup.find_all('a', href=True)
            
            for title in titles:
                print("Title:", title.text.strip())
            
            for link in links:
                print("Link:", link['href'])
            
            # Print the entire HTML page
            print("HTML Page Content:")
            print(response.text)
        else:
            print(f"Failed to retrieve page: {response.status_code}")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Starting URL for the crawler
start_url = 'https://example.com'

# Call the crawl_page function with the starting URL
crawl_page(start_url)
