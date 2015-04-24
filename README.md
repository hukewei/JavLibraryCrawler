# JavLibraryCrawler

This project allows you to scrape all movies from the javLibrary.
It  crawl the following items:
* Title
* Designation
* URL to the library website
* list of category
* Release Date
* Duration
* Actor
* Cover image URL
* Cover image hash value

It will also download cover image in local and generate the corresponded thum, you can configurate the image setting in [settings](https://github.com/hukewei/JavLibraryCrawler/blob/master/javLibraryCrawl/settings.py).

The tutorial for the image settings can be found [here](http://doc.scrapy.org/en/latest/topics/images.html).

##Install

* Install pip [from here](https://pip.pypa.io/en/latest/installing.html).

* Install scrapy [from here](http://doc.scrapy.org/en/latest/intro/install.html).

* Install dependencies:
```
pip install -r requirements.txt
```

##Run
This project contains two type of crawlers:

* Best rated movies (best_rated_spider)

* ALL movies (actor_spider)

To start the crawlers, please run : 
Crawl only best rated movies (500 movies) :
```
scrapy crawl best_rated_spider
```
or crawl all movies in the library(> 150000 movies, the somme of all cover images is around 16 GB ).
```
scrapy crawl actor_spider
```

##Credit
This project uses the [scrapy](https://github.com/scrapy/scrapy) to build the crawlers.


