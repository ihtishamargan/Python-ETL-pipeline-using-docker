
from sqlalchemy import create_engine
import pandas as pd
import requests
import dotenv
import os
from utility import extract, load, transform

def pg_connect():
    dotenv.load_dotenv()
    db_name = os.getenv('DB_NAME')
    db_user = os.getenv('DB_USER')
    db_password = os.getenv('DB_PASSWORD')
    db_host = os.getenv('DB_HOST')
    db_port = os.getenv('DB_PORT')
    engine = create_engine(f'postgresql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}')
    return engine


if __name__ == '__main__':

    url = "https://www.mphil.de/en/concerts-tickets/calendar#j16448"
    r = requests.get(url)
    soup = bs(r.content, 'html.parser')
    data = extract(soup)
    concerts_df = pd.DataFrame(data, columns=['Date_Time', 'Venue', 'Artists', 'Works', 'Img_Link'])
    concerts_df = transform(concerts_df)
    concerts_df = concerts_df.reindex(columns=['Date','Time','Venue', 'Artists', 'Works', 'Img_Link'])
    engine = pg_connect()    
    load(concerts_df, engine)