from findatapy.market import Market, MarketDataRequest, MarketDataGenerator
from pymongo import MongoClient
import datetime
# import pymongo
# import pprint


import config



start = '1 JAN 2015'
end = '1 NOV 2017'
symbol = 'eurusd'

start = datetime.datetime.strptime(start, '%d %b %Y')
current_start = start 
end = datetime.datetime.strptime(end, '%d %b %Y')





def process_batch(start, end, symbol):
	market = Market(market_data_generator=MarketDataGenerator())
	md_request = MarketDataRequest(start_date=start, finish_date=end,
	                                   category='fx', fields=['bid', 'ask'], freq='tick',
	                                   data_source='dukascopy', tickers=[symbol.upper()])

	df = market.fetch_market(md_request)
	print(df.tail(n=5))

	df.reset_index(level=0, inplace=True)
	df.columns = ['_id','bid','ask']
	print(df.tail(n=5))

	dc = df.to_dict('records')

	print("converted to dict")

	if config.mongo['user'] == "" or config.mongo['pasw'] == "":
		mongouri = "mongodb://"+config.mongo['uri']+":27017"
	else:
		mongouri = "mongodb://"+config.mongo['user']+":"+config.mongo['pasw']+"@"+config.mongo['uri']+":27017/admin"

	print(mongouri)

	client = MongoClient(mongouri)

	db = client['prices-data']
	# db = client['tests']
	collection = db[symbol.lower()+'_ticks']

	insert = collection.insert_many(dc)

	# doc= collection.find_one({})
	# print(insert)
	return insert


while current_start < end:
	print (current_start)
	current_end = current_start + datetime.timedelta(days=7)

	print (process_batch(start=current_start, end=current_end, symbol=symbol))
	current_start =current_end