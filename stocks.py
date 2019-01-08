import requests
import json
from io import StringIO
data_type = 'TIME_SERIES_DAILY'
symbol = 'MSFT'
apiKey = 'R47YKWQC9N8YJS1P'
interval = '1min'
outputsize = 'compact'
outputsizefull = 'full'

"""
data = requests.get('https://www.alphavantage.co/query?function={}&symbol={}&interval={}&apikey={}&outputsize={}'.format(data_type, symbol, interval, apiKey, outputsizefull))

data_dict = data.json()

data_str = json.dumps(data_dict)

txtstr = open("stockdata.txt", 'w')
txtstr.write(data_str)

txtstr.close()
"""

data = open("stockdata.txt", 'r')

string_data = data.read()

d = json.loads(string_data)

time = 'Time Series (Daily)'

open_price = []
close_price = []

for i in d:
	for j in d[i]:
		#print(j)
		for k in d[i][j]:
			if k == '1. open':
				open_price.append(d[i][j]['1. open'])
			if k == '4. close':
				close_price.append(d[i][j]['4. close'])

for i in range(10):
	print(open_price[i])
	print(close_price[i])


#print(d[time]['2000-01-19']['1. open'])

#for day in d[time]:
#	print(day)





