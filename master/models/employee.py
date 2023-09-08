from django.db import models

# Create your models here.

# 社員テーブル
class Employee(models.Model):
    employee_no = models.CharField(verbose_name="社員番号", max_length=6)
    name = models.CharField(verbose_name="氏名", max_length=100)
    employee_code = models.CharField(verbose_name="社員コード", max_length=100)
    email = models.EmailField(verbose_name="メールアドレス", max_length=254, blank=True, null=True,)
    date_of_birth = models.DateField(verbose_name="生年月日", blank=True, null=True,)
    hire_date = models.DateField(verbose_name="入社日", blank=True, null=True,)
    retirement_date = models.DateField(verbose_name="退職日", blank=True, null=True,)
    updated = models.DateTimeField(verbose_name="更新日時", auto_now=True)
    created = models.DateTimeField(verbose_name="登録日時", auto_now_add=True)

    class Meta:
#        db_table = 'employee'
        verbose_name_plural = '社員マスター'
        ordering = ['-updated']
    
    def __str__(self):
        return str(self.name)
