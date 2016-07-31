'''
Created on 2016-6-15

@author: Seiger
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()    #url_manager-->UrlManager对象
        self.downloader = html_downloader.HtmlDownloader()    #HtmlDownloader对象
        self.parser = html_parser.HtmlParser()              #HtmlParser对象
        self.outputer = html_outputer.HtmlOutputer()        #HtmlOutputer对象

    
    def craw(self, root_url):              
        count = 1
        self.urls.add_new_url(root_url)      #UrlManager对象add_new_url method
        while self.urls.has_new_url():       #UrlManager对象has_new_url 判断有没有 URL
            try:
                new_url = self.urls.get_new_url()   #得到一个URL
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)   #下载URL HTML数据
                new_urls,new_data = self.parser.parse(new_url,html_cont)   #得到这个页面所有的URL以及需要采集的数据
                self.urls.add_new_urls(new_urls)                           #把得到的URLS添加进列表
                self.outputer.collect_data(new_data)                       #把收集的数据放进LIST
                
                if count == 50:
                    break
    
                count = count + 1
            except:
                print('craw failed')
  
            
        self.outputer.output_html()
    
    

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"     #起始URL
    obj_spider = SpiderMain()                              #爬虫对象
    obj_spider.craw(root_url)                              #调用爬虫方法
