'''
Created on 2016-6-15

@author: Seiger
'''
from baike_spider import url_manager, html_downloader, html_parser,\
    html_outputer


class SpiderMain(object):
    def __init__(self):
        self.urls = url_manager.UrlManager()    #url_manager-->UrlManager����
        self.downloader = html_downloader.HtmlDownloader()    #HtmlDownloader����
        self.parser = html_parser.HtmlParser()              #HtmlParser����
        self.outputer = html_outputer.HtmlOutputer()        #HtmlOutputer����

    
    def craw(self, root_url):              
        count = 1
        self.urls.add_new_url(root_url)      #UrlManager����add_new_url method
        while self.urls.has_new_url():       #UrlManager����has_new_url �ж���û�� URL
            try:
                new_url = self.urls.get_new_url()   #�õ�һ��URL
                print 'craw %d : %s' % (count,new_url)
                html_cont = self.downloader.download(new_url)   #����URL HTML����
                new_urls,new_data = self.parser.parse(new_url,html_cont)   #�õ����ҳ�����е�URL�Լ���Ҫ�ɼ�������
                self.urls.add_new_urls(new_urls)                           #�ѵõ���URLS��ӽ��б�
                self.outputer.collect_data(new_data)                       #���ռ������ݷŽ�LIST
                
                if count == 50:
                    break
    
                count = count + 1
            except:
                print('craw failed')
  
            
        self.outputer.output_html()
    
    

if __name__=="__main__":
    root_url = "http://baike.baidu.com/view/21087.htm"     #��ʼURL
    obj_spider = SpiderMain()                              #�������
    obj_spider.craw(root_url)                              #�������淽��
