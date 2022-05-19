import requests
from bs4 import BeautifulSoup

# Mentioned variable in the task
url_list = ["https://en.wikipedia.org/wiki/Humayun_Ahmed", "https://en.wikipedia.org/wiki/Leonardo_DiCaprio"]
search_tag = ["Ahmed in 2010", "DiCaprio"]


# Return all the image URL from HTML Content
def get_all_image_from_url(soup):
    # Find all the img tag of HTML content from the specified URL
    images = soup.find_all('img')
    list_image = []
    for img in images:
        # Extracting image name from img tag & making it in lowercase
        src = img['src']
        image_name = src.split('/')[-1].lower()
        # Extracting image alt attribute from img tag & making it in lowercase
        image_alt = img['alt'].lower()
        for search in search_tag:
            # Searching the given keyword with image name or image alter value
            if search.lower() in image_alt or search.lower() in image_name:
                # Store the image source
                list_image.append(src)
                print(src)
    return list_image


# Code starts with here
if __name__ == "__main__":
    for url in url_list:
        print("Image from: " + url)
        # Getting response from given URL
        response = requests.get(url)
        if response.status_code == 200:
            # BeautifulSoup return HTML Content in soup variable
            soup = BeautifulSoup(response.content, 'lxml')
            image_url = get_all_image_from_url(soup)
        else:
            print("Invalid URL")
        print()
