# English Synonyms Crawler

*On 13th July 2020*

> Today I was talking with a friend who said he needed to find synonyms for english words, a matter of work. He was trying a machine learning approach. So I googled "english synonyms corpus" and it delivered me to http://thesaurus.com. Nice website! I didn't know it.
>
> Then I developed this little project, and by the way refresh some Scrapy concepts.

It's worth to mention that Thesaurus has its own API to get synonyms. It's described [here](http://thesaurus.altervista.org/service). But as I told above, I decided to develop this crawler to review some concepts.

To run the crawler:
```
scrapy crawl syno -a words_file=words.txt -o output.json
```


## Requirements

- [Scrapy 2.2](https://docs.scrapy.org/en/2.2/)
