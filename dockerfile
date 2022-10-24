FROM python:3.9

RUN pip install pandas sqlalchemy psycopg2 requests beautifulsoup4

WORKDIR /app

COPY ingest_data.py ingest_data.py
COPY wait-for-it.sh wait-for-it.sh 

ENTRYPOINT ["./wait-for-it.sh", "pgdatabase:5432", "--", "python", "ingest_data.py"]