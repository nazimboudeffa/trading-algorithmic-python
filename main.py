import yfinance as yf
import matplotlib.pyplot as plt
import pandas as pd 

fig, ax = plt.subplots()

def macd(df):
    df['EMA12'] = df.Close.ewm(span=12).mean()
    df['EMA26'] = df.Close.ewm(span=26).mean()
    df['MACD'] = df.EMA12 - df.EMA26
    df['signal'] = df.MACD.ewm(span=9).mean()
    print('indicators added')

def main():
    dfm30 = pd.DataFrame(yf.download('EURUSD=X', interval='30m', period="1d"))

    macd(dfm30)

    plt.plot(dfm30.signal, label='Signal', color='red')
    plt.plot(dfm30.MACD, label='MACD', color='green')

    fig.savefig('images/macd.png')

# launch main.py
    
if __name__ == '__main__':
    main()

