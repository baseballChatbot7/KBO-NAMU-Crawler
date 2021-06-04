#%%
import requests
from bs4 import BeautifulSoup
import time

def url2soup(url):
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}
    res = requests.get(url, headers=headers)
    if res.status_code == 429:
        time.sleep(int(res.headers["Retry-After"]))
        print(f'Blocked! Sleep for {int(res.headers["Retry-After"])}')
        return

    if res.status_code == 404:
        print('Not Found for page')
        return
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


# %%
def save_player_file(url):

    time.sleep(1)
    soup = url2soup(url)

    headings = soup.find_all(['h2', 'h3', 'h4'], attrs={'class':'wiki-heading'})
    # contents = (i.get_text() for i in soup.find_all('div', attrs={'class':'wiki-heading-content'}))
    contents = (i for i in soup.find_all('div', attrs={'class':'wiki-heading-content'}))
    file_name = soup.find('h1').get_text().strip()
    if file_name == '나무위키':
        return

    f = open(f'/Users/jb/workspace/webscrapping/player/{file_name}.txt', 'w')
    
    for head, content in zip(headings, contents):
        # internal_link = head.find('a', attrs={'class': 'wiki-link-internal'})
        # if internal_link:
        #     content = hyperlink2txt('https://namu.wiki' + internal_link['href'])
        #     content = '\n'.join(content)
        internal_link = content.find('a', attrs={'class': 'wiki-link-internal'})
        if internal_link:
            title = internal_link['title']
            if ('경력' in title) or (file_name in title):
                content = hyperlink2txt('https://namu.wiki' + internal_link['href'], file_name)
                content = '\n'.join(content)
            else:
                content = content.get_text()
        else:
            content = content.get_text()    
        head = head.get_text()
        f.write(head+'\n')
        f.write(content+'\n')
    print(f'{file_name} Save')

def hyperlink2txt(url, file_name):
    soup = url2soup(url)

    headings = (i.get_text() for i in soup.find_all(['h2', 'h3', 'h4'], attrs={'class':'wiki-heading'}))
    contents = (i for i in soup.find_all('div', attrs={'class':'wiki-heading-content'}))
    txt = []
    for heading, content in zip(headings, contents):
        internal_link = content.find('a', attrs={'class': 'wiki-link-internal'})
        if internal_link:
            title = internal_link['title']
            if ('경력' in title) or (file_name in title):
                content = hyperlink2txt_second('https://namu.wiki' + internal_link['href'])
                content = '\n'.join(content)
            else:
                content = content.get_text()
        else:
            content = content.get_text()
        txt.append(heading + '\n' + content)
    # print(soup.find_all('span', attrs={'class':'footnote-list'}))
    # footnote = (i.get_text() for i in soup.find_all('span', attrs={'class':'footnote-list'}))
    # print(txt)
    # txt.extend(list(footnote))
    return txt

def hyperlink2txt_second(url):
    soup = url2soup(url)

    headings = (i.get_text() for i in soup.find_all(['h2', 'h3', 'h4'], attrs={'class':'wiki-heading'}))
    contents = (i.get_text() for i in soup.find_all('div', attrs={'class':'wiki-heading-content'}))
    txt = []
    for heading, content in zip(headings, contents):
        txt.append(heading + '\n' + content)
    # print(soup.find_all('span', attrs={'class':'footnote-list'}))
    # footnote = (i.get_text() for i in soup.find_all('span', attrs={'class':'footnote-list'}))
    # print(txt)
    # txt.extend(list(footnote))
    return txt
# %%
def get_player_links(url):
    soup = url2soup(url)
    
    hrefs = []
    trs = soup.find_all('tr')
    for ts in trs:
        try:
            link = ts.a['href']
        except:
            continue
        hrefs.append('https://namu.wiki' + link)
    return hrefs

def get_player_links_li(url):
    soup = url2soup(url)

    hrefs = []
    lis = soup.find_all('li')
    for li in lis:
        try:
            link = li.a['href']
        except:
            continue
        hrefs.append('https://namu.wiki' + link)
    return hrefs


# %%
def read_team_url():
    f = open('/Users/jb/workspace/webscrapping/club/team_url.txt', 'r')
    url_list = f.read().split('\n')
    f.close()
    for link in url_list:
        save_club_file(link)

def save_club_file(url):
    soup = url2soup(url)

    headings = (i.get_text() for i in soup.find_all(['h2', 'h3'], attrs={'class':'wiki-heading'}))
    contents = (i.get_text() for i in soup.find_all('div', attrs={'class':'wiki-heading-content'}))
    file_name = soup.find('h1').get_text().strip()
    f = open(f'/Users/jb/workspace/webscrapping/club/{file_name}.txt', 'w')
    for h, c in zip(headings, contents):
        f.write(h+'\n')
        f.write(c+'\n')
    print(f'{file_name} Save')

# %%
url = 'https://namu.wiki/w/%EC%95%BC%EA%B5%AC%20%EA%B4%80%EB%A0%A8%20%EC%9D%B8%EB%AC%BC(KBO)'
links = get_player_links(url)
#%%
for link in links[:]:
    save_player_file(link)
# %%
url = 'https://namu.wiki/w/%EC%95%BC%EA%B5%AC%20%EA%B4%80%EB%A0%A8%20%EC%9D%B8%EB%AC%BC(KBO)'
links = get_player_links_li(url)
#%%
for link in links[5:]:
    save_player_file(link)
