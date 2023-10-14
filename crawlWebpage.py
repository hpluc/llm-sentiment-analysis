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
start_url = 'https://news.google.com/rss/articles/CBMifmh0dHBzOi8vd3d3LmZyLmRlL3BvbGl0aWsvdWtyYWluZS1rcmllZy1iYWNobXV0LWtyaW0tZ2VmZWNodGUtZ2VnZW5vZmZlbnNpdmUtcnVzc2xhbmQtbW9za2F1LWtpZXctbmV3cy10aWNrZXItenItOTI1NTQwMTMuaHRtbNIBAA?oc=5' #'https://example.com'

# Call the crawl_page function with the starting URL
crawl_page(start_url)
