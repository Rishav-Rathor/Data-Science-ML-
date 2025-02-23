import scrapy

class QuotesSpider(scrapy.Spider):
    name = "quotes_spider"

    def start_requests(self):  # Corrected method name
        urls = [
            "https://quotes.toscrape.com/page/1/",
            "https://quotes.toscrape.com/page/2/",
        ]
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):  # Moved outside start_requests
        page = response.url.split("/")[-2]
        filename = f'quotes-{page}.html'  # Using f-string

        
        # with open(filename, 'wb') as f:
        #     f.write(response.body)
        # self.log(f'Saved file {filename}')
