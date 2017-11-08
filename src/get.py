from findatapy.market import Market, MarketDataRequest, MarketDataGenerator
import pymongo
from pymongo import MongoClient
import pprint
import json

import config

#variables


t 
# dc['ask'] = dc.pop('EURUSD.ask')
# dc['bid'] = dc.pop('EURUSD.bid')
# dc.keys()


mongouri = "mongodb://"+config.mongo['user']+":"+config.mongo['pasw']+"@"+config.mongo['uri']+":27017/admin"
print(mongouri)
client = MongoClient(mongouri)

db = client['prices-data']
# db = client['tests']
collection = db['gbpjpy_ticks']

insert = collection.insert_many(dc)

# doc= collection.find_one({})
pprint.pprint(insert)