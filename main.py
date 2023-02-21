import urllib.request
import requests
import time
import ssl
import random

from datetime import datetime
def openUrl(ip, agent):
    headers = {'User-Agent': agent}
    proxies = {'http': ip}
    ######################################################################################################################
    requests.get("https://blog.csdn.net/Blackcat0/article/details/128847175", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/121763723", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/121649491", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcaat0/article/details/121627750", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/121137998", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/120847823", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/120840813", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/120068389", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/120068017", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/118605403", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/118220872", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/118220096", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112722881", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112628013", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112627876", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112587118", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112585941", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112583770", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112547800", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112531134", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112510580", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/104400002", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/104400067", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/104400177", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/104400177", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/109863946", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/109909071", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/109909365", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/109999622", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/109999962", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110000273", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110090941", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110091214", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110144106", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110144323", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110426493", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110480738", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110561077", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/110678061", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/111225464", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/111355218", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112472520", headers=headers, proxies=proxies,
                 verify=True)
    requests.get("https://blog.csdn.net/Blackcat0/article/details/112512659", headers=headers, proxies=proxies,
                 verify=True)
    ########################################################################################################################
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Access to success.",datetime.now())


def randomIP():
    ip = random.choice(['120.78.78.141', '122.72.18.35', '120.92.119.229'])
    return ip


# User-Agent
# User-Agent来源：http://www.useragentstring.com/pages/useragentstring.php
def randomUserAgent():
    UserAgent = random.choice(
        ['Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
         'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
         'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.0 Safari/537.36'])
    return UserAgent


if __name__ == '__main__':
    for i in range(999999):
        ip = randomIP()
        agent = randomUserAgent()
        openUrl(ip, agent)
        time.sleep(10)


