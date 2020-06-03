# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class IMDbYearItem(scrapy.Item):
    # define the fields for your item here like:
    movie_name = scrapy.Field()
    movie_id = scrapy.Field()
    movie_url = scrapy.Field()
    poster = scrapy.Field()
    year = scrapy.Field()
    genre = scrapy.Field()
    runtime = scrapy.Field()
    certificate = scrapy.Field()
    rating = scrapy.Field()
    metascore = scrapy.Field()
    plot = scrapy.Field()
    votes = scrapy.Field()
    gross = scrapy.Field()
    director = scrapy.Field()
    director_id = scrapy.Field()
    director_url = scrapy.Field()
    cast = scrapy.Field()
    cast_id = scrapy.Field()
    cast_url = scrapy.Field()
