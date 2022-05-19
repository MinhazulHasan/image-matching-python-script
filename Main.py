import requests
from bs4 import BeautifulSoup

url_list = ["https://en.wikipedia.org/wiki/Humayun_Ahmed", "https://en.wikipedia.org/wiki/Leonardo_DiCaprio"]
search_tag = ["Ahmed in 2010", "DiCaprio"]


# Return HTML Content
def get_content_from_url(response):
    soup = BeautifulSoup(response.content, 'lxml')
    return soup


# Return all the image URL from HTML Content
def get_all_image_from_url(soup):
    images = soup.find_all('img')
    list_image = []
    for img in images:
        src = img['src']
        image_name = src.split('/')[-1].lower()
        image_alt = img['alt'].lower()
        for search in search_tag:
            if search.lower() in image_alt or search.lower() in image_name:
                list_image.append(src)
                print(src)
    return list_image


if __name__ == "__main__":
    for url in url_list:
        print("Image from: " + url)
        response = requests.get(url)
        if response.status_code == 200:
            soup = get_content_from_url(response)
            image_url = get_all_image_from_url(soup)
        else:
            print("Invalid URL")
        print()
