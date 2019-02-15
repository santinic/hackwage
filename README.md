# hackwage
Hackwage is a RSS/JSON aggregator and search-engine for IT Jobs.
It can be easily adapted for other projects, maybe fetching different data sources.

The website is based on Python/Django and ElasticSearch, while data ingestion runs on NodeJS.

## How to run it (Debian)

#### Git clone
```
$ git clone https://github.com/santinic/hackwage.git
$ cd hackwage
```

#### Create Python Virtual Env
```
$ virtualenv -p python3 venv3
$ source venv3/bin/activate
$ pip install -r requirements.txt
```

#### Run ElasticSearch
Install ElasticSearch on your Debian,
[as documented here]([https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html]).
```
$ systemctl service start elasticsearch.service
```

#### Start fetching data
You need to run the script

#### Setup and run Django server
```
$ python manage.py migrate
$ python manage.py runserver
```

Now you should be able to access hackwage on you local machine on port 8000.