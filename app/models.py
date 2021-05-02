from django.db import models


# Create your models here.

class GetData(models.Model):
    title = models.CharField(verbose_name='标题', max_length=128)
    content = models.TextField(verbose_name='内容')
    add_time = models.CharField(verbose_name='添加时间', max_length=32)
    editor = models.CharField(verbose_name='编辑', max_length=32)

    class Meta:
        verbose_name = "爬虫数据表"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title
