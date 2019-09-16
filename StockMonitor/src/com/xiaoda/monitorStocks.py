'''
Created on 2019年9月15日

@author: xiaoda

实际执行股票的监控

'''

if __name__ == '__main__':
    pass


from com.xiaoda.monitor.stMonitor import StockMonitor
from com.xiaoda.monitor.mtThread import MonitorThread
from com.xiaoda.dataType.stDataType import StockDataType


'''
monitor = StockMonitor('sina', '601318')
monitor.monitorStock()
'''





#创建不同的线程，监控不同的股票

#设定监控间隔时间
timeInterval = 30

'''
#中国平安
stData1 = StockDataType('中国平安', '601318', 85, 9999)
monitor1 = StockMonitor('sina', timeInterval, stData1)#对601318股票进行监测，设定上下限价格，超过或达到则邮件提醒,设定监控间隔
print("线程构造完毕")
thread1 = MonitorThread( monitor1)
thread1.start()
'''


'''
stockDict = {"601318":StockDataType('中国平安', '601318', 85, 9999)}
stockDict.update("600036":StockDataType('招商银行', '6000036', 34, 9999))
'''

stockList = [StockDataType('中国平安', '601318', 85.00, 9999)]
stockList.append(StockDataType('招商银行', '600036', 34.00, 9999))
stockList.append(StockDataType('中信建投', '601066', 22.28, 9999))
stockList.append(StockDataType('中国人保', '601319', 8.16, 10.57))
stockList.append(StockDataType('华润三九', '000999', 24.99, 32.34))
stockList.append(StockDataType('华泰证券', '601688', 19.59, 25.35))
stockList.append(StockDataType('紫光股份', '000938', 30.82, 39.49))
stockList.append(StockDataType('东方财富', '300059', 14.00, 9999))
stockList.append(StockDataType('海康威视', '002415', 31.00, 9999))



for stock in stockList:
    #对股票按照设定的监控间隔进行监测，设定上下限价格，超过或达到则邮件提醒
    monitor = StockMonitor('sina', timeInterval, stock)
    thread = MonitorThread( monitor)
    thread.start()