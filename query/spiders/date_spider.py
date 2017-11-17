# -*- coding: utf-8 -*-

import scrapy
import os
from query.settings import URL
from query.settings import DATE_FILE

class PubSpider(scrapy.Spider):
    name = "date"
    def start_requests(self):
        # FormRequest 是Scrapy发送POST请求的方法
        yield scrapy.FormRequest(
            url = URL,
            callback = self.parse_page
        )
    def parse_page(self, response):
        if os.path.isfile(DATE_FILE):
            os.remove(DATE_FILE)
        # 写文件
        text = '''# -*- coding: utf-8 -*-
DATES = {}
TOTAL_NUMS = {}
'''
        file_object = open(DATE_FILE, 'w')
        file_object.write(text)
        file_object.close()
        #
        op_pattern = '//select[@id="issueNumber"]/option'
        for i in range(len(response.xpath(op_pattern))):
            date_pattern = op_pattern + '[{0}]/@value'.format(i+1)
            date = response.xpath(date_pattern).extract_first()
            # FormRequest 是Scrapy发送POST请求的方法
            yield scrapy.FormRequest(
                url = URL,
                formdata = {"pageNo" : "1", "issueNumber" : date},
                callback = self.parse_page2
            )

    def parse_page2(self, response):
        se_pattern = '//select[@id="issueNumber"]/option[@selected="selected"]/text()'
        sp_pattern = '//span[@class="f_orange"][1]/text()'
        tn_pattern = '//span[@class="f_orange"][2]/text()'
        date = response.xpath(se_pattern).extract_first()
        page_num = response.xpath(sp_pattern).extract_first()
        total_num = response.xpath(tn_pattern).extract_first()
        # 写文件
        if int(date):
            text = '''DATES['{0}'] = {1}
TOTAL_NUMS['{0}'] = {2}
'''
            text = text.format(date, page_num, total_num)
            file_object = open(DATE_FILE, 'a')
            file_object.write(text)
            file_object.close()






