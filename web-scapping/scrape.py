import requests
from bs4 import BeautifulSoup
import json
import os

# uvpce_staff = 'http://www.uvpce.ac.in/ce-faculty'
# url_r = requests.get(uvpce_staff)
# print(url_r.status_code)

# # make it readable using soup
# data_soup = BeautifulSoup(url_r.text, 'html.parser')
# # table of faculty details
# table = data_soup.find('table',{'class': 'views-view-grid cols-1'})
# tbody = table.tbody
# print(tbody.prettify())

def downlad_img(img_list):
    download_path = '/home/codal/mywork/python-practice/practice/web-scapping/images/'
    img_name = ""
    print("Downloading images . . . ")
    for img_link in img_list:
        img = requests.get(img_link)
        ext = '.jpg'
        img_name = (img_link.split('/')[-1].split('.')[0]) + ext

        # if image already exists then skip
        if os.path.exists(download_path+img_name):
            pass
        else:
            # print(img_name)
            with open(os.path.join(download_path,img_name),'wb') as file:
                # for chunk in img.iter_content(1024):
                #     file.write(chunk)
                file.write(img.content)
    print("Done")

def scarp_faculty_details():
    faculty_details =[]
    img_list = []

    uvpce_faculty = 'http://www.uvpce.ac.in/ce-faculty'
    url_r = requests.get(uvpce_faculty)

    # make it readable using soup
    data_soup = BeautifulSoup(url_r.text, 'html.parser')
    # table of faculty details
    table = data_soup.find('table',{'class': 'views-view-grid cols-1'})
    tbody = table.tbody

    print("Scrapping faculty details . . .")
    for tr in tbody.contents:
        obj = {}
        if tr.name == None:
            continue
        try :
            # profile Image link
            # print(tr.td.find('div',{'class': 'views-field-field-profile-image'}).img.get('src').split('?')[0])
            obj['img-src'] = tr.td.find('div',{'class': 'views-field-field-profile-image'}).img.get('src').split('?')[0]
            img_list.append(obj['img-src'])
            # faculty-name
            # print()
            obj['name'] = tr.td.find('div',{'class': 'views-field-title'}).text.strip(' \n\t')

            # faculty-designation
            # print()
            obj['designation'] = tr.td.find('div',{'class': 'views-field-field-present-designation'}).text.strip(' \n\t')

            # faculty-extension-no
            # print()
            obj['extension-no'] = tr.td.find('div',{'class': 'views-field-field-extension-no'}).div.text.strip(' \n\t')

            # faculty-email
            # print()
            obj['email'] = tr.td.find('div',{'class': 'views-field-field-email-address'}).text.strip(' \n\t')

            # facult-research-interests
            # print()
            obj['research-interests'] = tr.td.find('div',{'class': 'views-field-field-research-interests'}).div.text.strip(' \n\t Title:\xa0')
        except:
            pass
        faculty_details.append(obj)
        # print(faculty_details)
        # print(img_list)

    # store the data into json file
    with open('faculty_details.json','w+') as file:
        file.write(json.dumps(faculty_details, indent = 2))

    downlad_img(img_list)

scarp_faculty_details()
