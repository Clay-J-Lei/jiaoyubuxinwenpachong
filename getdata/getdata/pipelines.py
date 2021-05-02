# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from app.models import GetData


class GetdataPipeline:
    def process_item(self, item, spider):
        try:
            get = GetData.objects.filter(title=item['title'][0])
            if get:
                print("数据重复")
                pass
            else:
                # print(item['add_time'][0][0:10])
                GetData.objects.create(title=item['title'][0], content=item['content'][0],
                                       add_time=item['add_time'][0][0:10],
                                       editor=item['editor'][0])
                print("save")
        except:
            print("中间件错误")
        return item
