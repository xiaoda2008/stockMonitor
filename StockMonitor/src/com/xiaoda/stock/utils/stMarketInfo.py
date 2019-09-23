'''
Created on 2019年9月16日

@author: picc
'''
import datetime
import tushare

class StockMarketInfo(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
    def isSmOpen(self):
        DatetimeNOW = datetime.datetime.now().strftime('%Y-%m-%d')
        OpenList = tushare.trade_cal()
        OpentimeList = OpenList.isOpen[OpenList.calendarDate == DatetimeNOW]
        #print(repr(OpentimeList))
        
        if OpentimeList.values[0] == 1:
            XianZaiShiJian = datetime.datetime.now().strftime('%H%M%S')
#            print(XianZaiShiJian)
#            print(93000<int(XianZaiShiJian)<150000)
            if 93000 < int(XianZaiShiJian) < 150000:
                return 1
            else:
                return 0
        else:
            return 0