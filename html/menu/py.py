
import requests
import time

t = ''
with open('result.txt','r') as f:
    t = f.readlines()
for i in t:
    print(i)
    r = requests.get(i, headers={
    'Cookie': r'_ga=GA1.3.260495326.1623039770; _gid=GA1.3.1054113249.1623039770; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22179e4b57b8e43a-0383f7da5ae1bac-49193101-3686400-179e4b57b8fdd3%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%22179e4b57b8e43a-0383f7da5ae1bac-49193101-3686400-179e4b57b8fdd3%22%7D; BSFIT_OkLJUJ=FIRqeP76w5KSBuHZPKF5-na-OMIVmYi1; UM_distinctid=179e4c33e205b8-0d77978e37e367-49193101-384000-179e4c33e21639; ZHh6ku4z=APZoteR5AQAAI6KEtwn97F5vAmxLXgluv0GXACVXUi7-an4dchwlrmdkIjFt|1|1|31465edda3b5fa8eabab1d93e15e23fccfe868bd; BSFIT_DEVICEID=NXY5U7TlCVnZnW_6He598Hmt12GFe79nPu9zFj0J4svC-FusMK2AtKL7NV1Rsju66mRgelT6LNe7iJZm98acSj-eQ3NBISZYdc0lUd75huPUHKSnZYKrCpZbOOCnV9xVAKDMDf2LaFdTncaOs7DfxVpZ9sZueqaM; BSFIT_EXPIRATION=1623114031818; fp_ver=4.8.4',
    'Accept': 'image/webp,image/png,image/svg+xml,image/*;q=0.8,video/*;q=0.8,*/*;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Host': 'www-static.chinacdn.starbucks.com.cn',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Safari/605.1.15',
    'Accept-Language': 'zh-CN,zh-Hans;q=0.9',
    'Referer': 'https://www.starbucks.com.cn/menu/',
    'Connection': 'keep-alive'})
    print(r.content)
    with open('../../images/'+i.split('/')[-1], 'wb') as image:
        image.write(r.content)
    time.sleep(2)
