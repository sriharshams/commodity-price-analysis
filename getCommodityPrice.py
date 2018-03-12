import sys
import numpy as np
import pandas as pd
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")



"""this method will get mean and variance of from data frame of
commodity prices for a given start_date & end_date"""
def getMeanVarianceOfCommodityPrice(df, start_date, end_date):
    start_date2 = datetime.strptime(start_date, '%Y-%m-%d').date()
    end_date2 = datetime.strptime(end_date, '%Y-%m-%d').date()

    # Select the rows between two dates
    in_range_df = df.loc[df["Date"].isin(pd.date_range(start_date2, end_date2))]
    in_range_df['Price'] = in_range_df['Price'].astype(str)
    in_range_df['Price'] = in_range_df['Price'].str.replace(',', '')
    in_range_df['Price'] = in_range_df['Price'].astype(float)

    mean = np.mean(in_range_df['Price'])
    variance = np.var(in_range_df['Price'])
    return mean, variance

def main():
    if len(sys.argv)!=4:
        # ./getCommodityPrice 2017-05-01 2017-05-03 gold
        print("Usage: python getCommodityPrice.py start_date(YYYY/MM/dd) end_date(YYYY/MM/dd) commodity")
        sys.exit(0)
    historical_data_commodity = None
    headers = ['Date', 'Price', 'Open', 'High', 'Low', 'Vol.', 'Change%']
    parse_dates = ['Date']
    fileName = ''

    if sys.argv[3] == 'gold':
        fileName = 'historical-gold.csv'
    elif sys.argv[3] == 'silver':
        fileName = 'historical-silver.csv'
    else :
        print("Usage: python getCommodityPrice.py start_date(YYYY/MM/dd) end_date(YYYY/MM/dd) commodity(gold|silver)")
        sys.exit(0)

    historical_data_commodity = pd.read_csv(fileName, sep='~', parse_dates=parse_dates, encoding ='utf-8')
    historical_data_commodity.columns= headers
    mean, variance = getMeanVarianceOfCommodityPrice(historical_data_commodity, sys.argv[1], sys.argv[2])

    print sys.argv[3], mean, variance
    sys.exit(0)


if __name__ == "__main__":
    main()
