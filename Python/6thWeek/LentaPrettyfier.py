"""
Принимает на вход ссылку(ссылки) на старницу lenta.ru с новостью.
Отдает файл html, где находится только контент статьи, ничего кроме.
Упрощает только страницы с новостями и со статьями. Спецматериалы не умеет.
"""
import re
import urllib.request

def get_page(url):
    page = urllib.request.urlopen(url)
    return page

def bin_2_str(page, charset):
    '''Gets page in binary, return str'''
    page_str = page.read().decode(charset)
    return page_str

def get_article(page_str):
    '''Gets all page, returns only article'''
    # Статья заканчивается социальными кнопками. Все что ниже нам не нужно.
    article = page_str.split('<section class="b-topic__socials">')[0]
    # Отсюда статья начинается
    if re.search('<div class="b-topic__content">', article):
        article = article.split('<div class="b-topic__content">')[-1]
        return article
    else:
        return False

def get_title(page_str):
    title = re.search('(?<=<title>).*?(?=</title>)', page_str, re.DOTALL)
    title = title.group()
    return title

def get_charset(page):
    '''Gets pages charset'''
    charset = page.getheader('Content-Type')
    charset = charset.split('=')[-1]
    return charset

def pretty_html(article, title):
    if article:
        filename = format_title(title)
        file = open(filename, 'w')
        file.write(article)
        file.close()
        print('Статья "' + title + '" записана в файл.')

def check_url(url):
    return re.match('http://lenta.ru/.*', url)

def format_title(string):
    # Чтобы Windows могла корректно записать title как название файла
    if len(string) > 250:
        string = re.search(r"^(\d+)", string).groups()[0] + ".html"
    else:
        string += ".html"
    return re.sub(r"[*|\:\"<>?/]", " ", string)

url_list = []

print("Введите одну или несколько (разделение по клавише Enter) \
ссылок на статьи с сайта lenta.ru\nВведите 'start' чтобы преобразовать")

while True:
    url = input('> ')
    if url == 'start':
        print('Преобразовываю ' + str(len(url_list)) + ' статей.')
        break
    if check_url(url):
        url_list.append(url)
    else:
        print('Неправильный линк')


fail = 0 # Счетчик неуспешных преобразований
for url in url_list:
    page = get_page(url)
    charset = get_charset(page)
    page_str = bin_2_str(page, charset)
    title = get_title(page_str)
    article = get_article(page_str)
    if article == False:
        fail += 1
    pretty_html(article, title)

print('Успешно преобразовано ' + str(len(url_list) - fail) +
      ' из ' + str(len(url_list)) + ' статей.')
