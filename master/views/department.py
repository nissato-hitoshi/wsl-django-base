from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView, FormView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.utils import timezone
import openpyxl
from datetime import datetime
from django.db.models import Q

from master.models import Department
from master.forms import DepartmentForm

class DepartmentListView(LoginRequiredMixin, ListView):
    template_name = 'master/department/index.html'
    model = Department
    paginate_by = 10
    context_object_name = 'items'

    def get_queryset(self):

        # sessionに値がある場合、その値でクエリ発行する。
        if 'search_value' in self.request.session:

            # セッションから検索情報取得
            search_value = self.request.session['search_value']

            # 検索条件
            condition1 = Q()
            condition2 = Q()

            # 検索文字が指定されている場合、条件設定
            if len(search_value) != 0:
                condition1 = Q(department_name__istartswith=search_value)
                condition2 = Q(department_code__istartswith=search_value)

            # 検索条件を指定して検索結果取得
            return Department.objects.select_related().filter(condition1 | condition2).order_by('display_order')

        else:
            # 検索条件指定なしの場合、全件取得
            return Department.objects.all().order_by('display_order')

    def get_context_data(self, **kwargs):
        print("get_context_data in")
        context = super().get_context_data(**kwargs)

        search_value = ''

        # sessionに値がある場合、その値をセットする。（ページングしてもform値が変わらないように）
        if 'search_value' in self.request.session:
            search_value = self.request.session['search_value']
        
        context['search_value'] = search_value

        return context

    def import_department(self, upload_file):
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

                # 同じ部門コードのデータ取得
                result = Department.objects.filter(department_code=str(ws.cell(row=i, column=1).value))

                # 同じ部門コードデータ存在確認
                if not result.exists():

                    # 存在しない場合、新規登録
                    item = Department(
                        department_code = ws.cell(row=i, column=1).value,
                        department_name = ws.cell(row=i, column=2).value,
                        display_order = ws.cell(row=i, column=3).value,
                    )

                    insert_items.append(item)
                else:
                    # 存在する場合、更新
                    item = result.get()
                    
                    item.department_name = ws.cell(row=i, column=2).value
                    item.display_order = ws.cell(row=i, column=3).value
                    item.updated = datetime.now()

                    update_items.append(item)

                i = i + 1

            # 更新リストデータが存在する場合
            if len(update_items) > 0:
                Department.objects.bulk_update(update_items, ['department_name', 'display_order', 'updated'])

            # 新規リストデータが存在する場合
            if len(insert_items) > 0:
                Department.objects.bulk_create(insert_items)

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
                if not self.import_department(upload_file):
                    print('import_department Error !!')

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

class DepartmentCreateView(LoginRequiredMixin, CreateView):
    template_name = 'master/department/create.html'
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('master.department.index')

class DepartmentUpdateView(LoginRequiredMixin, UpdateView):
    template_name = 'master/department/update.html'
    model = Department
    form_class = DepartmentForm
    success_url = reverse_lazy('master.department.index')
    context_object_name = 'item'

    def form_valid(self, form):
        Department = form.save(commit=False)
        Department.updated = timezone.now()
        Department.save()
        return super().form_valid(form)

class DepartmentDeleteView(LoginRequiredMixin, DeleteView):
    template_name = 'master/department/delete.html'
    model = Department
    success_url = reverse_lazy('master.department.index')
    context_object_name = 'item'
