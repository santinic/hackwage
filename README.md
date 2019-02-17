# hackwage
Hackwage is a RSS/JSON aggregator and search-engine for IT Jobs.
It can be easily adapted for other projects, for example to fetch and search News.

The website is based on Python/Django and ElasticSearch, while the live data is ingested via NodeJS.

[<kbd><img src="imgs/screenshot.png" width="600"></kbd>](https://hackwage.com)

## How to run it (Debian)

#### Create Python Virtual Env
```
$ git clone https://github.com/santinic/hackwage.git
$ cd hackwage
$ virtualenv -p python3 venv3
$ source venv3/bin/activate
$ pip install -r requirements.txt
```

#### Run ElasticSearch
Install the latest ElasticSearch on your Debian box,
[as documented here](https://www.elastic.co/guide/en/elasticsearch/reference/current/deb.html).
Then start it:
```
$ systemctl service start elasticsearch
```

#### Setup NodeJS and start ingesting data
```
$ cd node
$ npm install
$ npm run ingest
```
The script will try to fetch all the default data sources, you shouldn't get any error at this stage.

#### Setup a Cron Job
You can set up a cronjob to fetch data every hour.
Just run `crontab -e` and add a line like this:
```
0 * * * * cd /hackwage-path/node/ && npm run ingest >/dev/null 2>&1
```

#### Setup and run Django server
```
$ ln -s dj/dev_settings.py dj/settings.py
$ python manage.py migrate
$ python manage.py runserver
```

Now you should be able to access hackwage on you local machine on port 8000.


#### Django-cacheback
If you want to run the website in production, you might need to configure
django-cacheback and Celery to speed up the home page.
Basically this module tries to prepare asynchronously the homepage every hour,
so that is served from cache when the user arrives.
```
$ sudo apt install pyhton-celery-common
```
You can setup Celery to run via Systemd
[as explained here](http://docs.celeryproject.org/en/latest/userguide/daemonizing.html#usage-systemd).


## Todo

- Dockerize everything with Docker Compose