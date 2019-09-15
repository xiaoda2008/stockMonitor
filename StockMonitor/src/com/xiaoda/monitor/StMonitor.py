'''
Created on 2019年9月15日

@author: xiaoda
'''
import easyquotation
import json
import time
from com.xiaoda.utils.EmSender import EmailSender


class StockMonitor(object):
    '''
    监控指定数据源、指定股票的监控器
    '''


    def __init__(self, dataSource, timeInterval, stockData):
        '''
        dataSource:股票数据来源
        timeInterval:监控间隔秒数
        stockData:股票信息
        '''
        self.dataSource = dataSource
        self.stockData = stockData
        self.timeInterval = timeInterval
        self.monitorName = '股票 ' + self.stockData.stName + '(' \
        + self.stockData.stCode + ')' + ' 监控器'

    def monitorStock(self):
    
        print(self.monitorName + " 开始运行")
        sender = EmailSender()
    
        while True:
            quotation = easyquotation.use(self.dataSource)
            #snapshot = quotation.market_snapshot(prefix=True)
    
            real = quotation.real(self.stockData.stCode)#中文
            #print(real)
            json_str = json.dumps(real)
            stockSetdata = json.loads(json_str)
            #print(json_str)
            #print(stockSetdata['601318'])
            
            stdt = json.loads(json.dumps(stockSetdata[self.stockData.stCode]))
            #print('现价：', stdt['now'])
            #time.sleep(3) 

            if(stdt['now'] >= self.stockData.uPrice):
                mailSubject = stdt['name'] + " 超越  " + repr(self.stockData.uPrice) + "!, 抛出!!!" 
                mailContent = "当前时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"\
                + "股票代码：" + self.stockData.stCode + "\n"  \
                + "股票名称：" + stdt['name'] + '\n' \
                + "当前价格：" + repr(stdt['now'])
                sender.sendMails(mailSubject, mailContent)
                break

            if(stdt['now'] <= self.stockData.fPrice):
                mailSubject = stdt['name'] + " 低于  " + repr(self.stockData.fPrice) + "!, 买入!!!" 
                mailContent = "当前时间：" + time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + "\n"\
                + "股票代码：" + self.stockData.stCode + "\n"  \
                + "股票名称：" + stdt['name'] + '\n' \
                + "当前价格：" + repr(stdt['now'])
                sender.sendMails(mailSubject, mailContent)
                break
                
            
            time.sleep(self.timeInterval)
            
        print("已出发邮件提醒，" + self.monitorName +"结束运行！")







'''
bot = wxpy.Bot(cache_path=True) # 必须先登录过一次以后才可以使用缓存

friends=bot.friends()

attr=['男朋友','女朋友']
value=[0,0]
for friend in friends:
    if friend.sex == 1: # 等于1代表男性
        value[0]+=1
    elif friend.sex == 2: #等于2代表女性
        value[1]+=1

pie = pyecharts.charts.Pie("Egon老师的好朋友们")

pie.add("", attr, value, is_label_show=True)
pie.render('sex.html')
'''