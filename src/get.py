from findatapy.market import Market, MarketDataRequest, MarketDataGenerator
import pymongo
from pymongo import MongoClient
import pprint
import json

import config

from findatapy.market import Market, MarketDataRequest, MarketDataGenerator

market = Market(market_data_generator=MarketDataGenerator())
for month in ['JAN','FEB', 'MAR','APR', 'MAY','JUN','JUL','AUG','SEP','OCT','NOV','DEC']:
	print(month)


md_request = MarketDataRequest(start_date='1 FEB 2016', finish_date='1 JUN 2016',
                                   category='fx', fields=['bid', 'ask'], freq='tick',
                                   data_source='dukascopy', tickers=['GBPJPY'])

df = market.fetch_market(md_request)
print(df.tail(n=5))

df.reset_index(level=0, inplace=True)
df.columns = ['_id','bid','ask']
print(df.tail(n=5))

dc = df.to_dict('records')

if config.mongo['user'] == "" or config.mongo['pasw'] == "":
	mongouri = "mongodb://"+config.mongo['uri']+":27017"
else:
	mongouri = "mongodb://"+config.mongo['user']+":"+config.mongo['pasw']+"@"+config.mongo['uri']+":27017/admin"

print(mongouri)

client = MongoClient(mongouri)

db = client['prices-data']
# db = client['tests']
collection = db['GBPJPY_ticks']

insert = collection.insert_many(dc)

# doc= collection.find_one({})
pprint.pprint(insert)