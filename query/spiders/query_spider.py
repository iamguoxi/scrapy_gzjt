# -*- coding: utf-8 -*-

import scrapy
import os
from query.settings import URL
from date import DATES
from query.settings import QUERY_FILE
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )

class PubSpider(scrapy.Spider):
    name = "query"
    def start_requests(self):
        if os.path.isfile(QUERY_FILE):
            os.remove(QUERY_FILE)
        # 写文件
        text = '''# -*- coding: utf-8 -*-
QUERY = {}
'''
        file_object = open(QUERY_FILE, 'w')
        file_object.write(text)
        file_object.close()
        # FormRequest 是Scrapy发送POST请求的方法
        for date, page_num in DATES.items():
            for i in range(int(page_num)):
                yield scrapy.FormRequest(
                    url = URL,
                    formdata = {"pageNo" : str(i), "issueNumber" : date},
                    callback = self.parse_page
                )
    def parse_page(self, response):
        tr_pattern = '//table[contains(@class, "ge2_content")]/tr'
        for i in range(len(response.xpath(tr_pattern))):
            num_pattern = tr_pattern + '[{0}]/td[1]/text()'.format(i+1)
            name_pattern = tr_pattern + '[{0}]/td[2]/text()'.format(i+1)
            num = response.xpath(num_pattern).extract_first()
            name = response.xpath(name_pattern).extract_first()
            if num and name:
                # 写文件
                text = '''QUERY['{0}']='{1}'
'''
                text = text.format(num, name)
                file_object = open(QUERY_FILE, 'a')
                file_object.write(text)
                file_object.close()






