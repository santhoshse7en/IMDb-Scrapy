## IMDb_Scraper
A fun projects made using Scrapy. The Spiders included in this are able to extract Movie, TV-Series, TV-Movies based on year and title type. A lot more to come features ahead

## Run

### Create and activate virtual env 

**Python3**

```python

>> python3 -m venv venv
>> . ./venv/bin/activate

```

**Anaconda**

```python

>> conda create --name venv
>> conda activate venv

```

### Dependencies

* Scrapy

### Extracted information

IMDb Scraper extracts the following attributes from IMDb websites. Also, have a look at an examplary [json](https://github.com/santhoshse7en/IMDb_Scraper/blob/master/example/sample.json) and [CSV](https://github.com/santhoshse7en/IMDb_Scraper/blob/master/example/sample.csv) file extracted by IMDb Scraper.

* Movie Name
* Movie ID
* Movie URL
* Poster
* Year
* Genre
* RunTime
* Certificate
* Rating
* MetaScore
* Plot
* Votes
* Gross
* Director
* Director ID
* Director URL
* Cast
* Cast ID
* Cast URL

### Install dependencies

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install following

```python

>> pip install -r requirements.txt
>> pip install scrapy

```

**Anaconda**

```python

>> conda install scrapy -y

```

### TitleType was the main parameter to different title alongside release year to sort the release

* feature
* tv_series
* tv_movie
* tv_episode
* tv_special
* tv_miniseries
* documentary
* video_game
* short
* video
* tv_short

### Usage

```python

>> scrapy crawl imdb_year -a title_type=feature -a year=2019

```

**Save the output as a file**

```python

>> scrapy crawl imdb_year -a title_type=feature -a year=2019 -o output.csv

>> scrapy crawl imdb_year -a title_type=feature -a year=2019 -o output.json

```
