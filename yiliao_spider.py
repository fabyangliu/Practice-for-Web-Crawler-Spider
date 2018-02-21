import requests
from lxml import etree
from fake_useragent import UserAgent
from pymongo import MongoClient

def get_html_text(url):
    try:
        headers = {'User-Agent' : ua.random }
        r = requests.get(url ,headers = headers) #伪装成不同的访问请求头
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "异常"

if __name__ == "__main__" :
    ua = UserAgent()
    title_list = []
    spe_list = []
    for i in range(1,3): #只爬取了前两页
        url = 'http://www.999ask.com/list/yingyanbaojian/all/%d.html'%i
        s = etree.HTML(get_html_text(url))
        href_list = s.xpath('/html/body/div[5]/div[2]/div[4]/div[2]/ul/li/span[1]/a[2]/@href')
        print('处理第%d页'%i)
        for index,href in enumerate(href_list):
            url = 'http://www.999ask.com/' + href
            s = etree.HTML(get_html_text(url))
            str_list1 = s.xpath('/html/body/div[5]/div[2]/div[1]/div[1]/p/text()')
            title_list.extend(str_list1)
            str_list2 = s.xpath('/html/body/div[5]/div[2]/div[1]/div[2]/div[2]/p[2]/text()')
            spe_list.extend(str_list2)
            print('→正在处理第%d条'%(index + 1),str_list1,str_list2)
    client = MongoClient()
    db = client.health
    my_set = db.set
    my_set.insert({'问题':title_list ,'详情描述':spe_list})
    print('数据入库成功！')