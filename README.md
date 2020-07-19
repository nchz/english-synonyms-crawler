# English Synonyms Crawler

*On 13th July 2020*

> Today I was talking with a friend who said he needed to find synonyms for english words, a matter of work. He was trying a machine learning approach. So I googled "english synonyms corpus" and it delivered me to http://thesaurus.com. Nice website! I didn't know it.
>
> Then I developed this little project, and by the way refresh some Scrapy concepts.

It's worth to mention that Thesaurus has its own API to get synonyms. It's described [here](http://thesaurus.altervista.org/service). But as I told above, I decided to develop this crawler to review some concepts.


## Requirements

- [Python 3.7](https://docs.python.org/3.7/)
- [Scrapy 2.2](https://docs.scrapy.org/en/2.2/)


## Setup

All you need is to install the requirements:
```
pip install -r requirements.txt
```

Remember it is always recommended to use [virtual environments](https://docs.python.org/3.7/tutorial/venv.html).


## Play

First, you need to store your target words in the file `words.txt`, one word per line. A sample file is provided.

To run the crawler:
```
scrapy crawl syno -a words_file=words.txt -o output.json
```

You may also look for antonyms using the `type` argument:
```
scrapy crawl syno -a type=antonyms -a words_file=words.txt -o output.json
```

This argument may not be fully passed. It checks a `startswith` condition, so you can just pass `-a type=a`, or `-a type=ant`. Same thing for `synonyms`.
