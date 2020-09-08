from bs4 import BeautifulSoup
import requests

#send request
main_url="https://en.wikipedia.org/w/index.php?title=Category:Male_actors_in_Malayalam_cinema"
main_page=requests.get(main_url)
soup=BeautifulSoup(main_page.text,'html.parser')
category=soup.find('div', class_='mw-category')
th_tag=[]
td_tag=[]
#read a tag and capture href link
links = []
for link in category.find_all('a'):
    links.append(link.get('href'))

#list of links
root='https://en.wikipedia.org{}'
list_of_urls=[]
for i in links:
    list_of_urls.append(root.format(i))
    #print(list_of_urls)

for url in list_of_urls:
    # You can access the url in this loop with the name 'url'
    page = requests.get(url)
    soup = BeautifulSoup(page.text, "html.parser")
    infobox = soup.find_all('table', class_='infobox biography vcard')
    print(infobox)
    th_tag_var = soup.find_all('th', scope='row')
    for item in th_tag_var:
        th_tag.append(item.text)




#with open('info_html.html', 'r') as info:
 #   th_tag_var = info.find_all('th', scope='row')
   #  print(th_tag_var)


#td_tag=td_tag[1:]
