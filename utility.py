from bs4 import BeautifulSoup as bs
import pandas as pd



def extract(soup):
    list_concerts = soup.find_all("li", attrs = 
                                {'class':'mp16_cal-listitem card__vertical opas-list-element'})
    data = []
    for concert in list_concerts:
        date_time = str(concert.find('time', attrs={'class':'concert__date'}).string)
        venue = str(concert.find('div', attrs= {'class':'concert__venue'}).string)
        artists = concert.find('h2', attrs= {'class':'thetitles'}).text.replace('\n', ' ').strip()
        artists = artists.replace('\t',' ').strip()
        works = concert.find('div', attrs={'class':['mp_popbesetzung','mp_poptitel']}).text.replace('\n', ' ').strip()
        works = works.replace('\t', ' ').strip()
        img_link = concert.find('figure', attrs={'class':['card__image']}).a.get('href')
        data.append([date_time, venue, artists, works, img_link]) 
    return data

def transform(concerts_df):
    root_link = 'https://www.mphil.de/'
    concerts_df['Img_Link'] = root_link+concerts_df['Img_Link']
    concerts_df = format_datetime(concerts_df)
    concerts_df = concerts_df.drop(['Date_Time','Day'], axis = 1)
    concerts_df = concerts_df.reindex(columns=['Date','Time','Venue','Artists','Works','Img_Link'])
    return concerts_df

def format_datetime(concerts_df):
    concerts_df = concerts_df.join(concerts_df['Date_Time'].str.split(',', expand=True).rename(columns={0:'Day', 1: 'Date', 2:'Time'}))
    concerts_df['Date'] = pd.to_datetime(concerts_df['Date']).dt.date
    hour = concerts_df['Time'].str[:-5].str.replace('.', ':', 1).str.strip()
    am_pm = concerts_df['Time'].str[-5:].str.replace('.', '').str.strip()
    for i in range(len(hour)):
        if len(hour[i])<=2 :
            hour[i] = hour[i]+':00'
    concerts_df.Time = pd.to_datetime(hour +' '+ am_pm.str.replace('.', '').str.strip(), format='%I:%M %p').dt.time    
    return concerts_df

def load(data, engine):
    try:
        print('trying insert query')
        data.to_sql(name = 'concerts_data',  con = engine, if_exists= 'replace')
    except ValueError as err:
        print(err)
    else:
        print('Values added to Postgresql successfully')
