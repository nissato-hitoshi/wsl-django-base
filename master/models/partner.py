from django.db import models

# Create your models here.

# パートナーマスタテーブル
class Partner(models.Model):
    
    supplier_name = models.CharField(verbose_name="仕入先名", max_length=255, blank=False, null=False,)
    partner_name = models.CharField(verbose_name="パートナー名", max_length=100, blank=False, null=False, )
    partner_name_k = models.CharField(verbose_name="パートナー名(カナ)", max_length=100, blank=True, null=True, )
    description = models.CharField(verbose_name="備考", max_length=255, blank=True, null=True, )
    display_order = models.CharField(verbose_name="表示順", max_length=2, default='00', blank=False, null=False, )
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
#        db_table = 'cost'
        verbose_name_plural = 'パートナーマスター'
        ordering = ['-updated']

    def __str__(self):
        return str(self.partner_name)
