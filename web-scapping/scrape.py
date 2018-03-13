import requests
from bs4 import BeautifulSoup

# url = 'http://convert2mp3.net/en/'
#
# convert_url_base =  'http://convert2mp3.net/en/index.php?p=tags&id=youtube_Qvd43XKY-f0&key=bXDdu6wH0S1E'
# url2 = 'http://convert2mp3.net/en/index.php?p=complete&id=youtube_Qvd43XKY-f0&key=Tu4V6ocZeocS'
# youtube_url = 'https://www.youtube.com/watch?v=Qvd43XKY-f0'
# # requesting to that url


uvpce_staff = 'http://www.uvpce.ac.in/ce-faculty'
url_r = requests.get(uvpce_staff)
print(url_r.status_code)
# print(url_r.text)

# make it readable using soup
data_soup = BeautifulSoup(url_r.text, 'html.parser')
table = data_soup.findAll('table',{'class': 'views-view-grid cols-1'})
faculty_details =[]

for tab in table:
    tr_table = tab.findAll('tr')

    for row in tr_table:
        obj = {}
        # print(row)
        name = row.find('span', {'class':'field-content'}).text
        obj['name'] = name.strip(' ')
        faculty_details.append(obj)
        # print(text)
        img_src = row.find('img', src = True).get('src')
        # print(img_src)
print(faculty_details)

# download_url = data_soup.findAll('a',{'class': 'btn-success'}, href =True)
# print(download_url[0].get('href'))
