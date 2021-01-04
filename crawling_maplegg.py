import requests
from bs4 import BeautifulSoup

nickname = input('input your nickname: ')
webpage = requests.get('https://maple.gg/u/' + nickname)
soup = BeautifulSoup(webpage.content, 'html.parser')

simple_info = soup.find_all(attrs={'class':'user-summary-item'})
for i in range(0, 2):
    print(simple_info[i].get_text())
    
highest_floor = soup.find_all(attrs={'class':'character-card-additional-item'})
print(highest_floor[0].get_text()[9:-1])

floor_renewal_date = soup.find_all(attrs={'class':'user-summary-date'})
print(floor_renewal_date[0].get_text()[6:-1])

