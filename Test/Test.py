import requests

headers = {"authority": "www.jdl.cn", "scheme": "https", "path": "/order/getWaybillGisTrack",
           "accept": "*/*", "dnt": "1",
           "x-requested-with": "XMLHttpRequest",
           "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
           "origin": "https://www.jdl.cn", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors",
           "sec-fetch-dest": "empty",
           "referer": "https://www.jdl.cn/order/search?waybillCodes=JDVB08061439441",
           "accept-encoding": "gzip, deflate, br", "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
           "cookie": "pin=8970769768; unick=%E8%80%81%E5%91%B3%E9%81%93; thor=05947959F2CDF4B86057672DA7B20C45E49ADFBA53EEE9EE8B81CF7316939B49B4BA68D609E7684C84E5BC51B26F30B34FFC4EEB598D5583AA3EC95A604C10D106C7E9E447FDED9CF14527DD51A65BECE543F9F6ED601AF560FB64B64EEEBE8F11E7B35A9A9C781CA82F06736ED361FE4D4E90C074FA552B8A0CA8AB03095EA67285F2F376FE7A48C11199149C29B059; __jdv=130163593|www.google.com|-|referral|-|1613738136843; __jdc=130163593; __jda=130163593.16137381368421616037434.1613738137.1613738137.1613786867.2"}

cookies = {"pin": "8970769768", "unick": "%E8%80%81%E5%91%B3%E9%81%93",
           "thor": "05947959F2CDF4B86057672DA7B20C45E49ADFBA53EEE9EE8B81CF7316939B49B4BA68D609E7684C84E5BC51B26F30B34FFC4EEB598D5583AA3EC95A604C10D106C7E9E447FDED9CF14527DD51A65BECE543F9F6ED601AF560FB64B64EEEBE8F11E7B35A9A9C781CA82F06736ED361FE4D4E90C074FA552B8A0CA8AB03095EA67285F2F376FE7A48C11199149C29B059",
           "__jdv": "130163593|www.google.com|-|referral|-|1613738136843", "__jdc": "130163593",
           "__jda": "130163593.16137381368421616037434.1613738137.1613738137.1613786867.2"}

data = {"waybillCode": "JDVB08061439441&gpsTime=Feb+20%2C+2021+4%3A32%3A42+PM"}

print(requests.post("http://www.jdl.cn/order/getWaybillGisTrack", data=data, cookies=cookies).content)
