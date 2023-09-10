# Generated by Django 4.2.2 on 2023-09-06 03:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('master', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AccountingPeriod',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accounting_period', models.SmallIntegerField(verbose_name='会計期')),
                ('start_date', models.DateField(verbose_name='開始日')),
                ('end_date', models.DateField(verbose_name='終了日')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新日時')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'verbose_name_plural': '会計期間マスター',
                'ordering': ['-accounting_period'],
            },
        ),
    ]