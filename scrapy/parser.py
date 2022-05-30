import requests
from bs4 import BeautifulSoup
from django.views.decorators.csrf import csrf_exempt

HOST = "https://chasy.kg/"
HOST2 = "https://lalafo.kg/"

HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
}

@csrf_exempt
def get_html(url):
    req = requests.get(url=url,headers=HEADERS)
    return req


@csrf_exempt
def get_data_watch(html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all('div',class_="col-6 col-md-4 col-lg-4 col-xl-3 fm-item")
    watch = []

    for item in items:
        watch.append(
            {
                'link': item.find('div').find('a').get('href'),
                'image': item.find('div').find('img').get('src'),
                'title': item.find('div',class_='fm-module-title').get_text(strip=True)


            }


        )
    return watch


@csrf_exempt
def parser_func_watch():
    html = get_html(HOST)
    if html.status_code == 200:
        watch = []
        for i in range(0,1):
            watch.extend(get_data_watch(html.text))
            return watch
    else:
        raise  Exception("Error in parsr function")


@csrf_exempt
def get_data_lalafo(html):
    soup = BeautifulSoup(html,"html.parser")
    items = soup.find_all('article',class_="adTile-wrap")
    lalafo = []
    for item in items:
        lalafo.append(
            {
                "image": item.find('div').find('svg').get('xmlns'),
                "price": item.find('p',class_='adTile-price').get_text(),
                "title": 'http:/' + item.find('div').find('a').get('href'),
                "link":'http:/' + item.find('div').find('a').get('href')
            }
        )
    return lalafo

# html = get_html(HOST2)
# get_data_lalafo(html.text)

@csrf_exempt
def parser_func_lalafo():
    html = get_html(HOST2)
    if html.status_code == 200:
        lalafo = []
        for i in range(0,1):
            lalafo.extend(get_data_lalafo(html.text))
            return lalafo
    else:
        raise  Exception("Error in parsr function lalafo")
