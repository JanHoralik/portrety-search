import requests
from bs4 import BeautifulSoup

PAGES = 100

output = []
for page in range(0,PAGES):

    offset = str(10*page)
    url = 'https://hledani.rozhlas.cz/iRadio/?query=&reader=&porad%5B%5D=Portr%C3%A9ty&offset='+offset
    resp = requests.get(url, verify=False)
    #print(resp.text)

    b = BeautifulSoup(resp.text)
    uls = b.findAll('ul', {'class': 'box-audio-archive'})
    item = 0
    for ul in uls:
        #print(ul)
        downloadUrl = ''
        try:    
            download = ul.find('div', class_='action action-download')
            #print(download)
            downloadUrl = download.a['href']
        except:
            print('!!! Cannot parse href of offset: {0}, item: {1}'.format(offset, item))
        if not downloadUrl.startswith('https://plus.rozhlas.cz'):
            continue
        try:
            title = ul.findAll('img')[0]['title']
            #print(title)
            #print(downloadUrl)
            output.append('{0}, {1}'.format(title,downloadUrl))
        except:
            print('!!! Cannot parse title of offset: {0}, item: {1}'.format(offset, item))
        item +=1

print(output)
print(len(output))

        


#print(uls)



