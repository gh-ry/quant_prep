import pandas_datareader as pdr
import pandas as pd
import numpy as np
import os
from datetime import datetime
from pandas_datareader._utils import RemoteDataError
import requests

os.environ['ALPHA_ADV_API_KEY'] = '40RYIFDNNL516A41'
os.environ['TIINGO_API_KEY']    = 'ab4bdd46d831d409bdfae292566a900301dfc06b'
os.environ['IEX_API_KEY']       = 'pk_86df3e5ab20048e5a64416c67ec52984'
os.environ['QUANDL_API_KEY']    = 'JT2e2FFgvp7aGrPNxzs9'

'''
Get List of SP500 Companies
'''

table = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')
sp500_info = table[0]
sp500_info.to_csv('output/sp500_info.csv',index = False)
sp500_info.to_csv('output/sp500_symbols.csv',columns = ['Symbol'], index = False)


'''
read historical data from yahoo
'''

sp500_info = pd.read_csv('output/sp500_info.csv')
print ('Loading Historical Data ... ')

trunks = np.array_split(list(sp500_info.Symbol), 50)

i = 36
# process data one trunk at a time (~10 tickers), easier to find ticker causing problem #
for one_trunk in trunks:

    for one_ticker in one_trunk:
        one_ticker = one_ticker.replace('.','-')

        try: 
            one_data = pdr.data.DataReader(one_ticker, start='2010-10-1', end='2021-1-31', data_source='yahoo').reset_index()
            
        except RemoteDataError:
            print(one_ticker + ' Not Available')
            continue

        except KeyError:
            print(one_ticker + ' Not Available for this period')
            continue
        
        one_data['Symbol'] = one_ticker

        if one_ticker == one_trunk[0].replace('.','-'):
            df_hist = one_data
        else:
            df_hist = pd.concat([df_hist, one_data], axis = 0)

    df_hist = df_hist.reset_index(drop = True)

    df_hist.to_csv('output/historical_data_{}.csv'.format(i))

    i += 1


# merge all trunks #
path = "c:/Users/Ryan/Desktop/MyFolders/Work/quant_prep/output"
all_files = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
all_files = [f for f in all_files if 'historical_data' in f]

for one_file in all_files:
    one_data = pd.read_csv(os.path.join(path,one_file))
    one_data.drop(columns = ['Unnamed: 0'], inplace = True)
    
    if one_file == all_files[0]:
        df = one_data
    else:
        df = pd.concat([df,one_data], axis=0)

df.to_csv('output/sp500_2010_10_1_to_2021_1_31.csv')
