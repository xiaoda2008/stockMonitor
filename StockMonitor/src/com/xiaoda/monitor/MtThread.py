'''
Created on 2019年9月15日

@author: xiaoda
'''
import threading

class MonitorThread (threading.Thread):
    '''
    用于监控股票的线程
    '''
    def __init__(self, stockMonitor):
        threading.Thread.__init__(self)
        self.stockMonitor = stockMonitor
#        print("线程构造函数")
    def run(self):
#        print("开始运行线程")
        self.stockMonitor.monitorStock()
