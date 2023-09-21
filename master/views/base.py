from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils import timezone
from datetime import datetime

class BaseView():

    def nvl(self, value, default=''):
        if value is None:
            val = default
        else:
            val = str(value).strip()
        return val

    def convert_string_to_date(self, value, defalut=None):
        
        val = self.nvl(value, defalut)

        if val is not None:
            date_val = datetime.strptime(str(val), '%Y-%m-%d %H:%M:%S')
            val = date_val.strftime('%Y-%m-%d')

        return val

