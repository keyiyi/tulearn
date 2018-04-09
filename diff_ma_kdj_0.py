from utility import get_ma_2,ema2
from kdj_test import get_kd,ema_k
import tushare as ts
import random
import json
from multiprocessing import Pool
import datetime


def get_codes(category = 'zz500'):
    if category == 'hs300':
        filename = './hs300.json'
    else:
        filename = './zz500.json'
    with open(filename,'r') as f:
        content = json.load(f)
    code_list = list(content['code'].values())
    return code_list


def print_code_indicators(code):
    information = ts.get_k_data(code)
    ma_5_list = get_ma_2(information,5)
    ma_20_list = get_ma_2(information,20)
    ema12_list = ema2(information,12)
    ema26_list = ema2(information,26)
    k_list,d_list = get_kd(information)
    diff_list = [i-j for i,j in zip(ema12_list,ema26_list)]
    dea_list = ema_k(diff_list, 2 / 10)
    print('indicators for ',code,':')
    print('ma5:',ma_5_list[:5])
    print('ma20:', ma_20_list[:5])
    print('diff:', diff_list[:5])
    print('dea:', dea_list[:5])
    print('k_value:',k_list[:5])
    print('d_value:', d_list[:5])


def find_code(code,ma_codes,kd_codes,diff_codes):
    information = ts.get_k_data(code)
    ma_5_list = get_ma_2(information, 5)
    ma_10_list = get_ma_2(information, 10)
    ema12_list = ema2(information, 12)
    ema26_list = ema2(information, 26)
    k_list, d_list = get_kd(information)
    diff_list = [i - j for i, j in zip(ema12_list, ema26_list)]
    dea_list = ema_k(diff_list,2/10)
    # ma_codes= []
    # kd_codes = []
    # diff_codes= []
    if ma_5_list[0] > ma_10_list[0] and ma_5_list[1] < ma_10_list[1]:
        ma_codes.append(code)
    if 40>k_list[0] > d_list[0] and k_list[1] < d_list[1]:
        kd_codes.append(code)
    if 0>=diff_list[0] > dea_list[0] and diff_list[1] < dea_list[1]:
        diff_codes.append(code)
      

def find_save():
    ma_codes= []
    kd_codes = []
    diff_codes= []
    filename = datetime.datetime.now().strftime( '%y-%m-%d' )+'dmd.json'
    counter = 1
    code_list = get_codes('zz500')
    #code_list = random.sample(get_codes('zz500'), 100)
    for code in code_list:
        find_code(code,ma_codes,kd_codes,diff_codes)
        if counter %50 ==0 and counter < 499:
            print(counter ,'of code have been looked up, continue finding...')
        counter +=1
    print(len(ma_codes),'ma:',ma_codes)
    print(len(kd_codes),'kdj:',kd_codes)
    print(len(diff_codes),'macd:',diff_codes)
    data = {
        'ma_codes':ma_codes,
        'kd_codes':kd_codes,
        'macd':diff_codes
    }
    with open(filename,'w') as f:
        f.write(json.dumps(data))
    

if __name__ == '__main__':
    # for code in random.sample(get_codes('zz500'),3):
    #     print_code_indicators(code)
    #     print('----------------------------------')
    find_save()
    
   
    
    

