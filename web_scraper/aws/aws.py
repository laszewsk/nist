import scrapy
from awsscraper.items import Article
import pandas as pd

final_data = {}

class AiServicesSpider(scrapy.Spider):
    name = 'ai_services'
    allowed_domains = ['aws.amazon.com']
    start_urls = ['https://docs.aws.amazon.com/whitepapers/latest/aws-overview/machine-learning.html']

    def parse(self, response):
        art = Article()

        name_list = response.xpath('//h2/text()').getall()
        title_list = response.xpath('//h2/text()').getall()
        id_list = response.xpath('//h2/@id').getall()
        doc_list = response.xpath('//p/a/@href').getall()
      
        id_list_final = []
        for id in id_list:
            id = id.replace('amazon-','')
            temp=[]
            temp = id.split('-')
            print(temp)
            id_list_final.append(temp[-1])
        for id in id_list_final:
            if id == 'aws':
                id_list_final.remove(id_list_final[-1])
                id_list_final.append('tensorflow')

        doc_list_final = []
        for doc in doc_list:
            for id in id_list_final:
                if doc.endswith(id) or doc.endswith(id+'/'):
                    doc_list_final.append(doc)

        final_data['name'] = name_list
        final_data['title'] = title_list
        final_data['documentation'] = doc_list_final

        df = pd.DataFrame(final_data)
        df.to_csv('services.csv', index=False)