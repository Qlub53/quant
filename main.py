import tushare as tus
from pandas import DataFrame
import datetime
from talib import SMA
import traceback

tus.set_token('4b35b6b552ea66ef08186d267e693c86ed4726227979720aac8fb2d42a1c242a')
tl = tus.Master()
maPeriods = [10, 20, 60]


def mas_are_thrusted(ticker, date=datetime.datetime.now().strftime("%Y-%m-%d")):
    headDay = datetime.datetime.strftime(
        datetime.datetime.strptime(date, "%Y-%m-%d")
        - datetime.timedelta(days=365),
        "%Y-%m-%d"
    )

    dMktD = tus.get_k_data(ticker,headDay,date)
    if dMktD.empty:
        return False

    closed = dMktD['close'].values
    maVals = ma_vals(maPeriods,closed)

    todayOpen = dMktD['open'].values.tolist()[-1]
    todayClose = closed.tolist()[-1]
    return todayClose > max(maVals) and todayOpen < min(maVals)


def ma_vals(maperiods, closed):
    vals = []
    for ma in maperiods:
        val = SMA(closed,ma).tolist()[-1]
        vals.append(val)
    return vals


def trading_days_list():
    tl.TradeCal()
    return None


def all_stocks():
    return dict(tus.get_stock_basics()['name'])

if __name__ == '__main__':
    stocks = all_stocks()
    tickers = list(stocks.keys())
    tickers.sort()
    for ticker in tickers:
        if mas_are_thrusted(ticker):
            print("{}\t{}".format(ticker,stocks.get(ticker)))