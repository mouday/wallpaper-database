# -*- coding: utf-8 -*-
"""
@File    : main.py
@Date    : 2022-10-26
@Author  : Peng Shiyu
"""
import json
import os
from datetime import datetime

import bing_image


def main():
    data = bing_image.get_bing_image()
    date = datetime.strptime(data.get('date'), '%Y-%m-%d')

    dirname = date.strftime("%Y/%m")
    name = date.strftime("%d")
    filename = dirname + '/' + name + '.json'

    os.makedirs(dirname, exist_ok=True)

    with open(filename, 'w') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
