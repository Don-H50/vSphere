import time
import json
import requests
from urllib import parse,error
from scrapy import Selector
from urllib.parse import urlparse

CIS_list = []

url = "https://developer.vmware.com"
# domain_url = "https://developer.vmware.com/apis/vsphere-automation/latest/appliance/operation-index/"
# domain_url = "https://developer.vmware.com/apis/vsphere-automation/latest/cis/operation-index/"
# domain_url = "https://developer.vmware.com/apis/vsphere-automation/latest/content/operation-index/"
# domain_url = "https://developer.vmware.com/apis/vsphere-automation/latest/esx/operation-index/"
# domain_url = "https://developer.vmware.com/apis/vsphere-automation/latest/vapi/operation-index/"
# domain_url = "https://developer.vmware.com/apis/vsphere-automation/latest/vcenter/operation-index/"
domain_url = "https://developer.vmware.com/apis/vsphere-automation/latest/vstats/operation-index/"

header={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.80 Safari/537.36'}

onePage_text = requests.get(domain_url, headers=header).text
onePage_text_sel = Selector(text=onePage_text)

api_models = onePage_text_sel.xpath('//*[@id="doc-content-container"]/div/div[@class="clr-row"]')
print(api_models)
i = 0
for api_model in api_models:
    rest_api_url = []
    ways = []
    api_parts = api_model.xpath('./div[@class="clr-col-12"]')
    for api_part in api_parts:
        api_raws = api_part.xpath('./div/div[2]/div/table/tbody/tr')
        for api_raw in api_raws:
            api_dict = {}
            api_url_test = api_raw.xpath('./td[2]/a/@href').extract()[0]
            i = i + 1
            # 获取api段地址，进行拼接
            api_url = parse.urljoin(url, api_url_test)
            print(i, api_url)
            parsed_url = urlparse(api_url)
            # 获取api的请求方法
            api_method = parsed_url.path.rstrip('/').split('/')[-1]
            loop = 1
            get_api_page_text = ''
            while loop == 1:
                try:
                    loop = 0
                    get_api_page_text = requests.get(api_url, headers=header).text
                except error.URLError as error:
                    print(error.reason)
                    time.sleep(5)
                    loop = 1
            get_api_page_text_sel = Selector(text=get_api_page_text)
            # 获取api的请求路径
            api_path_list = get_api_page_text_sel.xpath('//*[@id="operation-api-path"]//text()').extract()[:]
            api_path = ''.join(api_path_list).strip()

            # 获取api请求头部
            api_header_para_string = get_api_page_text_sel.xpath('//*[@class="header-params-1"]//span[@class="param-name-txt"]/text()').extract()[0].strip()
            api_header_para_string_ex = ""
            post_api_request_body = get_api_page_text_sel.xpath('//*[@id="request-json-required"]/code')
            api_dict["method"] = api_method
            api_dict["api"] = api_path
            api_dict["Header_Parameters"] = api_header_para_string
            # api_dict["Header_Parameters_example"] = 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='
            if api_dict["Header_Parameters"] == "Authorization":
                api_dict["Header_Parameters_example"] = 'Basic dXNlcm5hbWU6cGFzc3dvcmQ='
            else:
                api_dict["Header_Parameters_example"] = 'sessionId'
            if post_api_request_body:
                post_api_request_body = post_api_request_body.xpath(".//text()").extract()[:]
                post_api_request_body = ''.join(post_api_request_body).strip().strip() .replace(" ", "").replace("\n", "").replace("\t", "")
                api_dict["Request_Body"] = post_api_request_body
            CIS_list.append(api_dict)
            print(i+100, api_method, api_path, api_header_para_string, api_header_para_string_ex, post_api_request_body)

print(CIS_list)

file_path = r'D:\Python\spider\REST_api_spider\vstats.json'  # 更改为你自己的路径和文件名

# 使用 'w' 参数打开文件进行写入
with open(file_path, 'w') as file:
    # 使用 json.dump 方法将数据写入文件
    json.dump(CIS_list, file, indent=4)
