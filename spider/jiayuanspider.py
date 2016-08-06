import requests
import logging
import json
from time import sleep

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                    datefmt='%a, %d %b %Y %H:%M:%S',
                    filename='../info.log',
                    filemode='w')

jiayuan_base_url = 'http://search.jiayuan.com/v2/search_v2.php'

user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0'


def get_maxpagenum(sex, cityId, age_from, age_to, pagenum=1):
    payload = {'sex': str(sex), 'key': '',
               'stc': '1:' + str(cityId) + ',2:' + str(age_from) + '.' + str(age_to) + ',23:1', 'sn': 'default',
               'sv': 1, 'p': str(pagenum), 'f': 'search',
               'listStyle': 'bigPhoto', 'pri_uid': 0, 'jsversion': 'v5'}
    headers = {'User-Agent': user_agent,
               'Host': 'search.jiayuan.com', 'Accept': '*/*', 'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
               'Accept-Encoding': 'gzip, deflate', 'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
               'X-Requested-With': 'XMLHttpRequest',
               'Referer': 'http://search.jiayuan.com/v2/index.php?sex=m&stc=1:' + str(cityId) + ',2:' + str(
                   age_from) + '.' + str(age_to) + ',23:1&f=search',
               'Connection': 'keep-alive', 'Cache-Control': 'max-age=0'}
    try:
        response = requests.post(jiayuan_base_url, data=payload, headers=headers, timeout=1)
    except:
        pass

    if response.status_code == 200:
        json_raw = json.loads(response.text.replace('##jiayser##//', '').replace('##jiayser##', ''))
        logging.debug(json_raw)
        maxpagenum = json_raw['pageTotal']
        return maxpagenum

    elif response.status_code == 403:
        logging.error('对方拒绝了您的请求，并向您扔了一个吻')


def crawl(sex, cityId, age_from, age_to):
    maxpagenum = get_maxpagenum(sex, cityId, age_from, age_to, 1)

    pagenum = 1
    while pagenum <= maxpagenum:
        print('正在爬取第 ' + str(pagenum) + ' 页的数据...')
        payload = {'sex': str(sex), 'key': '',
                   'stc': '1:' + str(cityId) + ',2:' + str(age_from) + '.' + str(age_to) + ',23:1', 'sn': 'default',
                   'sv': 1, 'p': str(pagenum), 'f': 'search',
                   'listStyle': 'bigPhoto', 'pri_uid': 0, 'jsversion': 'v5'}

        headers = {'User-Agent': user_agent,
                   'Host': 'search.jiayuan.com', 'Accept': '*/*',
                   'Accept-Language': 'zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3',
                   'Accept-Encoding': 'gzip, deflate',
                   'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
                   'X-Requested-With': 'XMLHttpRequest',
                   'Referer': 'http://search.jiayuan.com/v2/index.php?sex=m&stc=1:' + str(cityId) + ',2:' + str(
                       age_from) + '.' + str(age_to) + ',23:1&f=search',
                   'Connection': 'keep-alive', 'Cache-Control': 'max-age=0'}

        try:
            response = requests.post(jiayuan_base_url, data=payload, headers=headers, timeout=1)
        except:
            pass

        if response.status_code == 200:
            json_raw = json.loads(response.text.replace('##jiayser##//', '').replace('##jiayser##', ''))
            logging.debug(json_raw)

            '''write out to file'''
            with open('D:/世纪佳缘/女性用户/吉林/' + str(pagenum) + '.json', mode='w', encoding='utf-8') as f:
                f.write(str(json_raw['userInfo']))
                f.flush()
                f.close()

            maxpagenum = json_raw['pageTotal']

        elif response.status_code == 403:
            logging.error('对方拒绝了您的请求，并向您扔了一个吻')

        # sleep(2)
        pagenum += 1


if __name__ == '__main__':
    crawl('f', 22, 20, 28)
