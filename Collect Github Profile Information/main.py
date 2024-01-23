import requests
from bs4 import BeautifulSoup as bs

while True:
    github_user = input("Enter your github username: ")

    url = "https://github.com/" + github_user
    r = requests.get(url)
    soup = bs(r.content, "html.parser")
    profile_image = soup.find('img', {'class': 'avatar'})['src']
    print(profile_image)
    exit_code = input("Do you want to search another github username? (y/n): ")
    if exit_code == "y" or exit_code == 'Y':
        continue
    else:
        break
