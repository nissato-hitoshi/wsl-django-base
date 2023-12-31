from django.db import models

from .department import Department
from .grade import Grade
from .position import Position
from .employee import Employee
from .accounting_period import AccountingPeriod

# Create your models here.

# 所属マスタテーブル
class Affiliation(models.Model):
    accounting_period = models.ForeignKey(AccountingPeriod, on_delete=models.SET_NULL, null=True, verbose_name="会計期")
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, verbose_name="部門")
    position = models.ForeignKey(Position, on_delete=models.SET_NULL, null=True, verbose_name="役職")
    grade = models.ForeignKey(Grade, on_delete=models.SET_NULL, null=True, verbose_name="資格")
    employee = models.ForeignKey(Employee, on_delete=models.SET_NULL, null=True, verbose_name="氏名")
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
        verbose_name_plural = '所属マスター'
        ordering = ['department__display_order', 'position__display_order', 'grade__display_order']

    def __str__(self):
        return str(self.accounting_period) + ' : ' + str(self.department) + ' : ' + str(self.employee)
