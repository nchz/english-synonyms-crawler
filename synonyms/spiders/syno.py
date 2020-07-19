import scrapy


class SynoSpider(scrapy.Spider):
    name = 'syno'
    allowed_domains = ['thesaurus.com']

    def __init__(self, words_file, *args, **kwargs):
        super().__init__(*args, **kwargs)
        with open(words_file) as f:
            self.words = [w for w in f.read().splitlines() if w != '']

    def start_requests(self):
        for word in self.words:
            yield scrapy.Request(
                f'http://thesaurus.com/browse/{word}',
                callback=self.get_synonyms,
                meta={
                    'target_word': word,
                    'handle_httpstatus_list': [404],
                },
            )

    def get_synonyms(self, response):
        results = response.xpath('(//h2[contains(@class, "WordGridSectionHeading")])[1]'  # use [2] to get antonyms.
                                 '/following-sibling::ul[contains(@class, "WordGridLayoutBox")]'
                                 '/li/span/a/text()')
        if results != []:
            yield {response.meta['target_word']: [r.get() for r in results]}
        else:
            self.logger.warning(f'No results for "{response.meta["target_word"]}".')
