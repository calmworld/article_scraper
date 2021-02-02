import scrapy
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor 
from article_scraper.items import Article

class WikipediaSpider(CrawlSpider):
    name = 'wikipedia'
    allowed_domains = ['en.wikipedia.org']
    start_urls = ['https://en.wikipedia.org/wiki/Kevin_Bacon']

    rules = [
        Rule(LinkExtractor(allow=r'wiki/((?!:).)*$'), callback='parse_info', follow=True)
    ]

    def parse_info(self, response):
        article = Article()
        article['title']= response.xpath('//h1/text()').get() or response.xpath('//h1/i/text()')

        article['url']= response.url

        article['lastUpdated']= response.xpath('//li[@id="footer-info-lastmod"]/text()').get()
        return article



# first thing we want to do is extend Scrapy's crawlspider class instead of scrapy.spider
# what makes this a crawler instead of a scraper is using rules
# we can do this by using a scrapy rule object
# rule will take a scrapy link extractor object as it's argument
# it will also take the parse_info function
# and we will set follow to True for internal URLs - Keeps follwing and following urls
# (allow=r'wiki/((?!:).)*$') a regular expression meaning urls with wiki/sometext. excluding urls that contain colons in them