from django.db import models

from .affiliation import Affiliation

# Create your models here.

# 概算原価マスタテーブル
class Cost(models.Model):
    affiliation = models.ForeignKey(Affiliation, on_delete=models.SET_NULL, null=True, verbose_name="所属")
    cost1 = models.IntegerField(verbose_name="労務費", default=0)
    cost2 = models.IntegerField(verbose_name="通勤費", default=0)
    cost3 = models.IntegerField(verbose_name="間接労務費", default=0)
    cost4 = models.IntegerField(verbose_name="間接費配賦見込", default=0)
    cost_total = models.IntegerField(verbose_name="概算原価", default=0)
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
#        db_table = 'cost'
        verbose_name_plural = '概算原価マスター'
        ordering = ['-updated']

    def __str__(self):
        return str(self.cost_total)
