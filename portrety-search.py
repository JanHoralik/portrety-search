import requests
from bs4 import BeautifulSoup

PAGES_START = 0
PAGES = 100

output = []
errors = []
for page in range(PAGES_START,PAGES):

    offset = str(10*page)
    url = 'https://hledani.rozhlas.cz/iRadio/?query=&reader=&porad%5B%5D=Portr%C3%A9ty&offset='+offset
    resp = requests.get(url, verify=False)

    b = BeautifulSoup(resp.text)
    uls = b.findAll('ul', {'class': 'box-audio-archive'})
    item = 0
    for ul in uls:
        downloadUrl = ''
        try:    
            download = ul.find('div', class_='action action-download')
            downloadUrl = download.a['href']
        except:
            errors.append('!!! Cannot parse href of offset: {0}, item: {1}, content: {2}'.format(offset, item, download))
            continue

        if downloadUrl.startswith('https://plus.rozhlas.cz'):
            title = ul.findAll('img')[0]['title']
            output.append('{0}, {1}'.format(title,downloadUrl))
        elif downloadUrl.startswith('http://media.rozhlas.cz'):
            title = ul.find('div',class_='title').text
            output.append('{0}, {1}'.format(title,downloadUrl)) 
        else:
            print('!!! Unknown format of download URL, offset {0}, item {1}'.format(offset, item))
            print(ul)
        item +=1

print(output)
print(len(output))

print(errors)
print(len(errors))


        


#print(uls)



