import scrapy


WORD_LIST = [
    'tree',
    'circle',
]


class SynoSpider(scrapy.Spider):
    name = 'syno'
    allowed_domains = ['thesaurus.com']

    def start_requests(self):
        for word in WORD_LIST:
            yield scrapy.Request(
                f'http://thesaurus.com/browse/{word}',
                callback=self.get_synonyms,
            )

    def get_synonyms(self, response):
        for s in response.xpath('//h2[contains(@class, "WordGridSectionHeading")]'
                                '/following-sibling::ul[contains(@class, "WordGridLayoutBox")]'
                                '/li/span/a/text()'):
            print(f'###### {s.get()}')
