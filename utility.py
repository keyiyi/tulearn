import tushare as ts


def get_ma(stock_code,days = 5):
    ma_list = []
    information = ts.get_k_data(stock_code)['close'][-60:]
    for i in range(60-days+1):
        ma_price = information.iloc[i:i+days].mean()
        ma_list.append(float('% .2f' % ma_price))
    return ma_list


def get_ma_2(information,days =5):
    ma_list = []
    close_list = information['close'][-60:]
    for i in range(60 - days + 1):
        ma_price = close_list.iloc[i:i + days].mean()
        ma_list.append(float('% .2f' % ma_price))
    ma_list.reverse()
    return ma_list


    
def ema12(n):
    if n ==0:
        return price_list[0]
    else:
        return price_list[n]*alf1 + ema12(n-1)*(1 - alf1)

'''
def ema(price_list,days = 12):
    alf = 2 / (1+days)
    value = 0
    for i in range(len(price_list)):
        value += price_list[i] * (1-alf)**i

    return (alf * value)
'''
def ema(price_list,days = 12):
    alf = 2 / (1+days)
    ema_list = []
    value = 0
    for i in range(len(price_list)):
        value += price_list[i] * (1-alf)**i
    #ema_list.append(alf * value)
    ema_list.append(float('% .2f' % alf*value))
    for i in range(1,5):
        ema_list.append(float('% .2f' %((ema_list[i-1] - alf*price_list[i-1])/ (1-alf) )))
    return ema_list


def ema2(information,days = 12):
    alf = 2 / (1+days)
    price_list = list(information.sort_index(ascending=False)['close'])
    ema_list = []
    value = 0
    for i in range(len(price_list)):
        value += price_list[i] * (1-alf)**i
    # ema_list.append(alf * value)
    ema_list.append((alf * value))
    for i in range(1,int(len(price_list)*0.5)):
        # ema_list.append((ema_list[i-1] - alf*price_list[i-1])/(1-alf))
        ema_list.append((ema_list[i - 1] - alf * price_list[i - 1]) / (1 - alf))
    return ema_list


def ema_rec(n,days = 12):
    alf_in = 2 / (1+days)
    if n ==0:
        return price_list[0]
    else:
        return price_list[n]*alf_in + ema_days(n-1,days)*(1 - alf_in)
