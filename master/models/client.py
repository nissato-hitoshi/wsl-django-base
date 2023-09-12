from django.db import models

# Create your models here.

# 取引先マスタテーブル
class Client(models.Model):
    client_name = models.CharField(verbose_name="取引先名", max_length=100)
    client_name_s = models.CharField(verbose_name="取引先略称", max_length=20, blank=True, null=True, )
    display_order = models.CharField(verbose_name="表示順", max_length=2, default='00', blank=False, null=False, )
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
#        db_table = 'cost'
        verbose_name_plural = '取引先マスター'
        ordering = ['-updated']

    def __str__(self):
        return str(self.client_name)
