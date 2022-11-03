Following command can be used to build and run docker containers. 
```bash
docker-compose up
```

A postgresql container will be created and once it is available, a seperate container will be created to run ETL script 'ingest_data.py'. 

It will scrape website (extract), process data into a Pandas DataFrame (transform) and then will ingest into 'events' database (load).

To interact with database server, use following details.


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