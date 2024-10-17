import scrapy


class QuoteSpider(scrapy.Spider):
    name = "quote"
    # start_urls = ["https://quotes.toscrape.com"]

    def start_requests(self):
        yield scrapy.Request(f'https://quotes.toscrape.com/tag/{self.tag}')

    def parse(self, response, **kwargs):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield {
                'quote': quote.xpath('.//span//text()').get(),
                'author': quote.xpath('.//small[@class="author"]//text()').get(),
                'tag': quote.xpath('.//a[@class="tag"]//text()').getall()
            }

# agora vamos usar a scrapy real time - pip install scrapyrt
# http://localhost:9080/crawl.json?spider_name=quote&url=http://quotes.toscrape.com/
