from django.db import models

# Create your models here.

# 役職マスタテーブル
class Position(models.Model):
    position_name = models.CharField(verbose_name="役職名", max_length=50)
    position_code = models.CharField(verbose_name="役職コード", max_length=10, blank=True, null=True, )
    display_order = models.CharField(verbose_name="表示順", max_length=2, default='00', blank=False, null=False, )
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
#        db_table = 'position'
        verbose_name_plural = '役職マスター'
        ordering = ['-display_order']

    def __str__(self):
        return str(self.position_name)
