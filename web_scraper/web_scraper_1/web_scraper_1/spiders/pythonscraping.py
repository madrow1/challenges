import scrapy
import w3lib.html

class PythonscrapingSpider(scrapy.Spider):
    name = "pythonscraping"
    allowed_domains = ["pythonscraping.com"]
    start_urls = ["http://pythonscraping.com/linkedin/ietf.html"]

    def parse(self, response):
        return {"title": response.xpath('//meta[@name="DC.Title"]/@content').get(),
                "date": response.xpath('//span[@class="date"]/text()').get(),
                "number": response.xpath('//span[@class="rfc-no"]/text()').get(),
                "description": response.xpath('//meta[@name="DC.Description.Abstract"]/@content').get(),
                "text": w3lib.html.remove_tags(response.xpath('//div[@class="text"]/text()').get()),
                "headings": response.xpath('//span[@class="subheading"]/text()').getall()
        }
