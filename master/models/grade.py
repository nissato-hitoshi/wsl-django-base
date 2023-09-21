from django.db import models

# Create your models here.

# 資格マスタテーブル
class Grade(models.Model):
    grade_code = models.CharField(verbose_name="資格コード", max_length=10, blank=False, null=False, primary_key=True,)
    grade_name = models.CharField(verbose_name="資格名", max_length=50)
    display_order = models.CharField(verbose_name="表示順", max_length=2, default='00', blank=False, null=False, )
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
        verbose_name_plural = '資格マスター'
        ordering = ['-display_order']

    def __str__(self):
        return str(self.grade_name)
