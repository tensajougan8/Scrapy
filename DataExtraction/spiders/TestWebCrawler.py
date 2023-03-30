import scrapy
import pandas as pd
from scrapy import item


class TestSpider(scrapy.Spider):
    name = "quotes"
    data = pd.read_excel(r'Input.xlsx')
    df = pd.DataFrame(data, columns=['URL_ID','URL'])
    print([df['URL']])
    url = []
    for i in df['URL']:
        url.append(i)
    start_urls = url

    def parse(self, response):
        for quote in response.css('article.post'):
            yield {
                'title': quote.css('h1.entry-title::text').get(),
                'text': quote.css('p::text').getall(),
                'url': response.request.url
            }