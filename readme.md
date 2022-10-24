Following command can be used to run docker compose. 
```bash
docker-compose up
```

A postgresql container will be created and once it is available, a seperate container will be created to run script 'ingest_data.py'. 

It will scrape website, process data into a Pandas DataFrame and then will ingest into 'events' database.

To access the database, use following details.
### Postgresql:
```
user = 'root'
password = 'root'
host = 'pgdatabase'
port = 5432
db = 'events'

Table Name = 'concerts_data'

```

Data is scraped from the following web page:

url = "https://www.mphil.de/en/concerts-tickets/calendar#j16448"


## Table Schema:

```Table
Date (DATE)
Time (TIME)
Artists (TEXT)
Works (TEXT)
Img_Links (TEXT)

```