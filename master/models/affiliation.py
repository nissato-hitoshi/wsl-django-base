from django.db import models

from .department import Department
from .grade import Grade
from .position import Position
from .employee import Employee

# Create your models here.

# 所属マスタテーブル
class Affiliation(models.Model):
    accounting_period = models.SmallIntegerField(verbose_name="会計期", blank=False, null=False,)
    start_date = models.DateField(verbose_name="所属開始日", blank=False, null=False,)
    end_date = models.DateField(verbose_name="所属終了日", blank=False, null=False,)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="部門")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, verbose_name="役職")
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, verbose_name="資格")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="氏名")
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
#        db_table = 'affiliation'
        verbose_name_plural = '所属マスター'
#        ordering = ['-display_order']
