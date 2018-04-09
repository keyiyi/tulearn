def get_rsv(information,days):
    information = information.sort_index(ascending=False)
    high_list = list(information['high'])
    low_list = list(information['low'])
    close_list = list(information['close'])
    rsv9_list = []
    for i in range(len(information)-days):
        high_n = max(high_list[i:i+days])
        low_n = min(low_list[i:i+days])
        close_n = close_list[i]
        rsv = (close_n - low_n)/(high_n - low_n) *100
        rsv9_list.append(rsv)
    return rsv9_list


def ema_k(value_list,alf =1/3):
    value = 0
    ema_list = []
    for i in range(len(value_list)):
        value += value_list[i] * (1-alf)**i
    ema_list.append(alf * value)
    for i in range(1,int(len(value_list)*0.5)):
        value_n = (ema_list[i-1] - alf *value_list[i-1])/(1 - alf)
        ema_list.append(value_n)
    return ema_list


def get_kd(code_information):
    rsv_list = get_rsv(code_information,9)
    kvalue_list = ema_k(rsv_list)
    dvalue_list = ema_k(kvalue_list)
    return(kvalue_list,dvalue_list)
