import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd 

fig, ax = plt.subplots()

def MACD(df):
    df['EMA12'] = df.Close.ewm(span=12).mean()
    df['EMA26'] = df.Close.ewm(span=26).mean()
    df['MACD'] = df.EMA12 - df.EMA26
    df['signal'] = df.MACD.ewm(span=9).mean()
    print('indicators added')

df30 = pd.DataFrame(yf.download('EURUSD=X', interval='30m', period="1d"))

MACD(df30)

plt.plot(df30.signal, label='signal', color='red')
plt.plot(df30.MACD, label='MACD', color='green')

fig.savefig('images/macd.png')
