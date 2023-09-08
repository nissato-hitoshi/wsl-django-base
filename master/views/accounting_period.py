from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
import openpyxl
from datetime import datetime
from django.db.models import Q

from master.models import AccountingPeriod
from master.forms import AccountingPeriodForm

class AccountingPeriodListView(LoginRequiredMixin, ListView):
    template_name = 'master/accounting_period/index.html'
    model = AccountingPeriod
    paginate_by = 10
    context_object_name = 'items'

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

    def get_queryset(self):

        # sessionに値がある場合、その値でクエリ発行する。
        if 'search_value' in self.request.session:

            # セッションから検索情報取得
            search_value = self.request.session['search_value']

            # 検索条件
            condition1 = Q()

            # 検索文字が指定されている場合、条件設定
            if len(search_value) != 0:
                condition1 = Q(accounting_period__istartswith=search_value)

            # 検索条件を指定して検索結果取得
            return AccountingPeriod.objects.select_related().filter(condition1)

        else:
            # 検索条件指定なしの場合、全件取得
            return AccountingPeriod.objects.all()

    def get_context_data(self, **kwargs):
        print("get_context_data in")
        context = super().get_context_data(**kwargs)

        search_value = ''

        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        if 'search_value' in self.request.session:
            search_value = self.request.session['search_value']
        
        context['search_value'] = search_value

        return context

    def import_accounting_period(self, upload_file):

        try:
            # アップロードファイルのオープン
            wb = openpyxl.load_workbook(upload_file, data_only=True)

            # 「sheet1」シートを参照
            ws = wb['Sheet1']

            # 一括追加用配列
            insert_items = []
            update_items = []

            i = 2
            while i <= ws.max_row:

                # 会計期と氏名が同じデータ取得
                result = AccountingPeriod.objects.filter(accounting_period=int(ws.cell(row=i, column=1).value))

                # 同じデータ存在確認
                if not result.exists():

                    # 存在しない場合、新規登録
                    item = AccountingPeriod(
                        accounting_period = ws.cell(row=i, column=1).value,
                        start_date = self.convert_string_to_date(ws.cell(row=i, column=2).value, None),
                        end_date = self.convert_string_to_date(ws.cell(row=i, column=3).value, None),
                    )

                    insert_items.append(item)
                else:
                    # 存在する場合、更新
                    item = result.get()
                    
                    item.start_date = self.convert_string_to_date(ws.cell(row=i, column=2).value, None)
                    item.end_date = self.convert_string_to_date(ws.cell(row=i, column=3).value, None)
                    item.updated = datetime.now()

                    update_items.append(item)

                i = i + 1

            # 更新リストデータが存在する場合
            if len(update_items) > 0:
                print('update : ' + str(len(update_items)))
                AccountingPeriod.objects.bulk_update(update_items, ['start_date','end_date','updated'])

            # 新規リストデータが存在する場合
            if len(insert_items) > 0:
                print('insert : ' + str(len(insert_items)))
                AccountingPeriod.objects.bulk_create(insert_items)

            wb.close()
            rc = True

        except Exception as e:
            print('Exception In !!')
            print(e)
            rc = False

        finally:
            print('all finish')

        return rc

    def post(self, request, *args, **kwargs):

        try:
            # アップロード時
            if self.request.POST.get('mode', '') == 'upload':

                upload_file = self.request.FILES['upload_file']

                # 役職ファイルアプロード処理
                if not self.import_accounting_period(upload_file):
                    print('import_accounting_period Error !!')

            # 検索時
            elif self.request.POST.get('mode', '') == 'search':

                # セッションに検索値を設定
                request.session['search_value'] = self.request.POST.get('search_value', '')

        except Exception as e:
            print('Exception In !!')
            print(e)

        finally:
            print('all finish')

            # 検索時にページネーションに関連したエラーを防ぐ
            self.request.GET = self.request.GET.copy()
            self.request.GET.clear()
            return self.get(request, *args, **kwargs)

class AccountingPeriodCreateView(LoginRequiredMixin, CreateView):
    template_name = 'master/accounting_period/create.html'
    model = AccountingPeriod
    form_class = AccountingPeriodForm
    success_url = reverse_lazy('master.accounting_period.index')

class AccountingPeriodUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'master/accounting_period/update.html'
    model = AccountingPeriod
    form_class = AccountingPeriodForm
    success_url = reverse_lazy('master.accounting_period.index')
    context_object_name = 'item'

    def form_valid(self, form):
        Affiliation = form.save(commit=False)
        Affiliation.updated = timezone.now()
        Affiliation.save()
        return super().form_valid(form)

class AccountingPeriodDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'master/accounting_period/delete.html'
    model = AccountingPeriod
    success_url = reverse_lazy('master.accounting_period.index')
    context_object_name = 'item'
