WEEK 6
"The web is not a library, it's
a living organism. A crawler
is how we tame it."
WEB CRAWLING
Presented by Chhay Keokanitha
CS 382 - Search Engines and Information Retrieval

WEB CRAWLERS?
LIKE... SPIDERS?

LIKE SPIDER-MAN?
UMM... NO.

While it’d be cooler
if our crawlers
wore spandex and
fought crime, these
“spiders” spend
24/7 sneaking
through websites,
taking notes, and
obsessively
following every link
they find.

INTRODUCING
WEB CRAWLER
| A          | web  | crawler  |          | (also  | called  | a               | spider  | or  | bot)    | is  an |
| ---------- | ---- | -------- | -------- | ------ | ------- | --------------- | ------- | --- | ------- | ------ |
| automated  |      |          | program  |        | that    | systematically  |         |     | browses |        |
the web to collect and index content.
Real-World Examples:
→
|     | Googlebot  |     |     |  indexes the entire public web |     |     |     |     |     |     |
| --- | ---------- | --- | --- | ------------------------------ | --- | --- | --- | --- | --- | --- |
→
|     | Bingbot  |     |  Microsoft's search crawler |     |     |     |     |     |     |     |
| --- | -------- | --- | --------------------------- | --- | --- | --- | --- | --- | --- | --- |
→
|     | Common Crawl  |     |     |     |  open dataset of web pages |     |     |     |     |     |
| --- | ------------- | --- | --- | --- | -------------------------- | --- | --- | --- | --- | --- |
→
|     | Your  | Midterm  |     |     | Project  |     |   crawling  |     | targeted |     |
| --- | ----- | -------- | --- | --- | -------- | --- | ----------- | --- | -------- | --- |
domains for search
Key Question to Ask: What should we fetch, in what
order, and what do we do with it?

HOW DOES GOOGLE
FIND WEBSITES?

A crawler is basically a very curious robot with infinite patience.
Search engines use Crawlers visit pages
crawlers/spiders automatically
They follow links to They extract
discover more pages information

WHY WEB CRAWLING?
The Search Engine Pipeline:
→ → → → →
Crawl Parse Index Query Rank Return Results
WITHOUT A CRAWLER: CRAWLING CHALLENGES:
Billions of pages: which do you
No documents to index
visit first?
No corpus for TF-IDF
Pages change: when do you re-
No search engine
crawl?
Politeness: how fast can you go?
Traps: infinite URL loops

ARCHITECTURE OF A WEB CRAWLER
Seed URLs: Initial web pages to start
[Seed URLs] [URL Frontier / Queue]
the crawling process.
Example: https://quotes.toscrape.com/
[Fetcher / Downloader] URL Frontier (Queue): A queue contains
URLs to be downloaded/visited.
Fetcher/Downloader: Downloads the
[HTML Parser / Extractor]
HTML content from the webpage using
the fetched IP address.
Parser/Extractor: Parses HTML, extracts
[Data Store]
[New URLs]
(structured output)
(back to queue) text data, and checks if the content is
new or a duplicate.

THE POLITENESS PROBLEM
robots.txt - The Crawl Contract:
User-agent: *
Disallow: /private/
Crawl-delay: 2
Why does politeness matter?
Excessive requests can crash small
servers
Many sites block IPs that crawl too
aggressively
Ethical crawling = professional crawling

INTRODUCING
RULES OF THUMB
Always check robots.txt before crawling
Add delays between requests (1–3 seconds
minimum)
Identify your crawler with a proper User-Agent string
Do NOT crawl login-protected pages without
permission
Discussion: What happens if you ignore robots.txt?

URL FRONTIER STRATEGIES
| Breadth-First | Depth-First  | Best-First /   |
| ------------- | ------------ | -------------- |
| Search (BFS)  | Search (DFS) | Priority-Based |
Visit all links at depth Follow one path as Rank URLs by estimated
importance (PageRank,
| 1 before going deeper | deep as possible |     |
| --------------------- | ---------------- | --- |
topic relevance)
| Good for broad, | Risk: getting trapped |     |
| --------------- | --------------------- | --- |
Used in production
| shallow coverage | in infinite link |     |
| ---------------- | ---------------- | --- |
crawlers
| Risk: lots of low- | structures |     |
| ------------------ | ---------- | --- |
More complex to
| quality deep pages |     | implement |
| ------------------ | --- | --------- |
For our Midterm: We'll use BFS with depth limiting in Scrapy

INTRODUCING
SCRAPY
Python framework for large-scale
web crawling and scraping
→
Asynchronous fast and efficient
Built-in support for: pipelines,
middleware, item export
Install: !pip install scrapy
More Informations Here

SCRAPY TOOLS
|                     | Feature    | Scrapy       |     | BeautifulSoup |          | Selenium |         |
| ------------------- | ---------- | ------------ | --- | ------------- | -------- | -------- | ------- |
|                     | Speed      | Fast (async) |     |               | Moderate |          | Slow    |
|                     | Javascript |              | No  |               | No       |          | Yes     |
|                     | Scale      | Production   |     | Small Scripts |          |          | Testing |
| Built-in scheduling |            |              | Yes |               | No       |          | No      |

SCRAPY ARCHITECTURE
The Spider is the only part YOU write. Scrapy handles the rest.

COMPONENTS
|     | Scrapy Engine |     | Scheduler |     | Downloader |
| --- | ------------- | --- | --------- | --- | ---------- |
The engine is responsible The scheduler receives The Downloader is
for controlling the data requests from the engine responsible for fetching
| flow between all |     | and enqueues them for |     | web pages and feeding |     |
| ---------------- | --- | --------------------- | --- | --------------------- | --- |
components of the system, feeding them later (also to them to the engine which,
and triggering events when the engine) when the in turn, feeds them to the
| certain actions occur. |         | engine requests them. |               | spiders.               |     |
| ---------------------- | ------- | --------------------- | ------------- | ---------------------- | --- |
|                        | Spiders |                       | Item Pipeline | Downloader middlewares |     |
specific hooks that sit
 responsible for processing
Spiders are custom
between the Engine and the
the items once they have
classes written by Scrapy
Downloader and process
been extracted (or
| users to parse responses |     |     |     | requests when they pass |     |
| ------------------------ | --- | --- | --- | ----------------------- | --- |
scraped) by the spiders.
| and extract items from |     |     |     | from the Engine to the |     |
| ---------------------- | --- | --- | --- | ---------------------- | --- |
Typical tasks include
Downloader, and responses
them or additional
cleansing, validation and
that pass from Downloader
requests to follow.
|     |     | persistence. |     | to the Engine. |     |
| --- | --- | ------------ | --- | -------------- | --- |

CSS SELECTORS VS XPATH
CSS Selectors (simpler,
XPath (more powerful)
recommended)
response.css("div.quote response.xpath("//span[@clas
span.text::text").get() s='text']/text()").get()
response.css("a::attr(href)" response.xpath("//a/@href").
).getall() getall()

LET’S BUILD YOUR FIRST SPIDER
import scrapy
class QuotesSpider(scrapy.Spider):
name = "quotes" # Unique spider name
start_urls = ["https://quotes.toscrape.com/"]
def parse(self, response):
# Extract data using CSS selectors
for quote in response.css("div.quote"):
yield {
"text": quote.css("span.text::text").get(),
"author": quote.css("small.author::text").get(),
"tags": quote.css("a.tag::text").getall(),
}
# Follow next page link (crawling!)
next_page = response.css("li.next a::attr(href)").get()
if next_page:
yield response.follow(next_page, self.parse)
RUN IT
scrapy runspider quotes_spider.py -o quotes.json

SCRAPY ITEMS & PIPELINES
DEFINING A STRUCTURED ITEM OUTPUT FORMATS
import scrapy
# JSON
scrapy crawl quotes -o output.json
class
QuoteItem(scrapy.Item):
# CSV
text = scrapy.Field() scrapy crawl quotes -o output.csv
author = scrapy.Field()
tags = scrapy.Field() # JSON Lines
scrapy crawl quotes -o output.jsonl
url = scrapy.Field()
ITEM PIPELINE (SETTINGS.PY)
ITEM_PIPELINES = {
'myproject.pipelines.CleanTextPipeline': 300,}

SCRAPY SETTINGS: POLITENESS
# settings.py - important defaults to set
BOT_NAME = 'cs382_crawler'
# Respect robots.txt
ROBOTSTXT_OBEY = True
# Delay between requests (seconds)
DOWNLOAD_DELAY = 2
# Max concurrent requests
CONCURRENT_REQUESTS = 4
# User agent
USER_AGENT = 'CS382 Educational Bot
(+http://university.edu/cs382)'
# Limit crawl depth
DEPTH_LIMIT = 3
# Max pages per domain
CLOSESPIDER_PAGECOUNT = 100

LAB ASSIGNMENT
WHAT WE BUILT TODAY: WHAT COMES NEXT :
→
A functional Scrapy spider Take your crawled data build a
search engine on top of it
Extracted structured data
Implement TF-IDF to rank
(text, author, tags)
documents by relevance
Followed pagination links
→
Accept a query return the
Saved to JSON / CSV
most relevant crawled pages
Submit the Google Colab link
Submit: Colab notebook + written
to the Google Classroom
report + GitHub repo + video
demo

KEY TAKEAWAYS
A crawler has 5 components: seed URLs,
URL frontier, fetcher, parser, visited set
Politeness (robots.txt, delays) is non-
negotiable
Scrapy handles scheduling/downloading
- you only write the Spider
CSS selectors and XPath extract data
from HTML
Your crawled data becomes the corpus
for your midterm search engine.

WEEK 6
| T   | H   | A   | N   | K   |   Y | O   | U   |
| --- | --- | --- | --- | --- | --- | --- | --- |
FOR YOUR ATTENTION
Presented by Chhay Keokanitha
CS 382 - Search Engines and Information Retrieval

REFERENCES
Scrapy Documentation: https://docs.scrapy.org
Practice Site: https://quotes.toscrape.com
robots.txt spec: https://www.robotstxt.org
Manning & Schütze, Introduction to Information Retrieval, Ch. 20