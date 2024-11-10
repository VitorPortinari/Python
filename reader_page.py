import requests
from bs4 import BeautifulSoup

url = 'https://www.pg.unicamp.br/norma/31879/0'

# Send a GET request to the URL with SSL verification disabled
response = requests.get(url, verify=False)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    content_list = [p.text for p in soup.find_all('p')]
    print(content_list)
else:
    print(f"Failed to retrieve page. Status code: {response.status_code}")
