from django.db import models

# Create your models here.

# 会計期間マスタテーブル
class AccountingPeriod(models.Model):
    accounting_period = models.SmallIntegerField(verbose_name="会計期", blank=False, null=False,)
    start_date = models.DateField(verbose_name="開始日", blank=False, null=False,)
    end_date = models.DateField(verbose_name="終了日", blank=False, null=False,)
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
        verbose_name_plural = '会計期間マスター'
        ordering = ['-accounting_period']

    def get_accounting_period_display(self):
        return '{}期'.format(self.accounting_period)

    def get_accounting_period_title(self):
        return '{}期 ({:%Y年%m月%d日} ~ {:%Y年%m月%d日} )'.format(
                self.accounting_period, self.start_date, self.end_date)
    
    def __str__(self):
        return str(self.accounting_period)
    