import scrapy


class SynoSpider(scrapy.Spider):
    name = 'syno'
    allowed_domains = ['thesaurus.com']

    def __init__(self, words_file, type='synonyms', *args, **kwargs):
        super().__init__(*args, **kwargs)

        with open(words_file) as f:
            self.words = [w for w in f.read().splitlines() if w != '']

        if 'synonyms'.startswith(type.lower()):
            self.type = 1
        elif 'antonyms'.startswith(type.lower()):
            self.type = 2
        else:
            raise ValueError(f'Invalid crawler type: {type}. Options are: "synonyms" or "antonyms"')

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
        results = response.xpath(f'(//h2[contains(@class, "WordGridSectionHeading")])[{self.type}]'
                                 '/following-sibling::ul[contains(@class, "WordGridLayoutBox")]'
                                 '/li/span/a/text()')
        if results != []:
            yield {response.meta['target_word']: [r.get() for r in results]}
        else:
            self.logger.warning(f'No results for "{response.meta["target_word"]}".')
