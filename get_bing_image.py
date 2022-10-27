# -*- coding: utf-8 -*-
"""
@File    : spider.py
@Date    : 2022-10-26
@Author  : Peng Shiyu
"""
import json
import re

import requests


def get_bing_image():
    url = 'https://cn.bing.com'

    headers = {
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36'
    }

    res = requests.get(url, headers=headers)
    res.encoding = res.apparent_encoding

    ret = re.search("var _model =(\{.*?\});", res.text)
    if not ret:
        return

    data = json.loads(ret.group(1))
    image_content = data['MediaContents'][0]['ImageContent']

    return {
        'headline': image_content['Headline'],
        'title': image_content['Title'],
        'description': image_content['Description'],
        'image_url': image_content['Image']['Url'],
        'main_text': image_content['QuickFact']['MainText']
    }


if __name__ == '__main__':
    res = get_bing_image()
    print(json.dumps(res, ensure_ascii=False, indent=2))

