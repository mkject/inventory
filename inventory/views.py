from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import (
    View,
    CreateView, 
    UpdateView
)
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
# pemanggilan model
from .models import Stock,Modal,Pemasukkan,Pengeluaran,Keuangan
from .forms import StockForm,ModalForm,PemasukkanForm,PengeluaranForm
from django_filters.views import FilterView
from .filters import StockFilter
from openpyxl import Workbook
from django.http import HttpResponse 


class StockListView(FilterView):
    filterset_class = StockFilter
    queryset = Stock.objects.filter(is_deleted=False)
    template_name = 'inventory.html'
    paginate_by = 10

def export_excel(request):
    # Ambil data dari model Django
    data = Keuangan.objects.all()

    # Buat objek Workbook dari openpyxl
    workbook = Workbook()
    sheet = workbook.active

    # Menambahkan header kolom
    header = ["id", "Keterangan", "Jenis","Nominal"]
    sheet.append(header)

    # Menambahkan data dari model ke sheet Excel
    for item in data:
        row = [item.id, item.keterangan, item.jenisKeuangan,item.Nominal]
        sheet.append(row)

    # Tanggapi dengan file Excel yang akan diunduh
    response = HttpResponse(content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
    response["Content-Disposition"] = "attachment; filename=Laporan_Keuangan_akhir.xlsx"
    workbook.save(response)

    return response

class keuanganListView(FilterView):

    filterset_class = StockFilter
    ##menampilkan data model 
    queryset = Keuangan.objects.all()
    template_name = 'inventory_keuangan.html'
    paginate_by = 10
class PengeluaranListView(FilterView):
    filterset_class = StockFilter
    queryset = Pengeluaran.objects.filter(is_deleted=False)
    template_name = 'inventory_pengeluaran.html'
    paginate_by = 10

class PemasukkanListView(FilterView):
    filterset_class = StockFilter
    queryset = Pemasukkan.objects.filter(is_deleted=False)
    template_name = 'inventory_pemasukkan.html'
    paginate_by = 10
class ModalListView(FilterView):
    filterset_class = StockFilter
    queryset = Modal.objects.filter(is_deleted=False)
    template_name = 'inventory_modal.html'
    paginate_by = 10

class ModalCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Modal                                                                       # setting 'Stock' model as model
    form_class = ModalForm                                                              # setting 'StockForm' form as form
    template_name = "edit_modal.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory/inventory_modal'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Modal Baru'
        context["savebtn"] = 'Simpan'
        return context       

class ModalUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Modal                                                                       # setting 'Stock' model as model
    form_class = ModalForm                                                              # setting 'StockForm' form as form
    template_name = "edit_modal.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory/inventory_modal'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Modal has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Modal Modal'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Modal'
        return context

class StockCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Stock Baru'
        context["savebtn"] = 'Simpan'
        return context       


class StockUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Stock                                                                       # setting 'Stock' model as model
    form_class = StockForm                                                              # setting 'StockForm' form as form
    template_name = "edit_stock.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Stock has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Edit Stock'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Stock'
        return context


class StockDeleteView(View):                                                            # view class to delete stock
    template_name = "delete_stock.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Stock has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        stock = get_object_or_404(Stock, pk=pk)
        return render(request, self.template_name, {'object' : stock})

    def post(self, request, pk):  
        stock = get_object_or_404(Stock, pk=pk)
        stock.is_deleted = True
        stock.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory')

class ModalDeleteView(View):
    template_name = "delete_modal.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Modal has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        modal = get_object_or_404(Modal, pk=pk)
        return render(request, self.template_name, {'object' : modal})

    def post(self, request, pk):  
        modal = get_object_or_404(Modal, pk=pk)
        modal.is_deleted = True
        modal.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory_modal')

class PemasukkanUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Pemasukkan                                                                       # setting 'Stock' model as model
    form_class = PemasukkanForm                                                              # setting 'StockForm' form as form
    template_name = "edit_pemasukkan.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory/inventory_pemasukkan'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Modal has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Modal Modal'
        context["savebtn"] = 'Update Stock'
        context["delbtn"] = 'Delete Modal'
        return context

class PengeluaranUpdateView(SuccessMessageMixin, UpdateView):                                 # updateview class to edit stock, mixin used to display message
    model = Pengeluaran                                                                       # setting 'Stock' model as model
    form_class = PengeluaranForm                                                              # setting 'StockForm' form as form
    template_name = "edit_pengeluaran.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory/inventory_pengeluaran'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Pengeluaran has been updated successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Pengeluaran'
        context["savebtn"] = 'Update Pengeluaran'
        context["delbtn"] = 'Delete Pengeluaran'
        return context

class PengeluaranCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Pengeluaran                                                                       # setting 'Stock' model as model
    form_class = PengeluaranForm                                                              # setting 'StockForm' form as form
    template_name = "edit_pengeluaran.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory/inventory_pengeluaran'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Pemasukkan has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Pengeluaran Baru'
        context["savebtn"] = 'Simpan'
        return context   

class PemasukkanCreateView(SuccessMessageMixin, CreateView):                                 # createview class to add new stock, mixin used to display message
    model = Pemasukkan                                                                       # setting 'Stock' model as model
    form_class = PemasukkanForm                                                              # setting 'StockForm' form as form
    template_name = "edit_pemasukkan.html"                                                   # 'edit_stock.html' used as the template
    success_url = '/inventory/inventory_pemasukkan'                                                          # redirects to 'inventory' page in the url after submitting the form
    success_message = "Pemasukkan has been created successfully"                             # displays message when form is submitted

    def get_context_data(self, **kwargs):                                               # used to send additional context
        context = super().get_context_data(**kwargs)
        context["title"] = 'Pemasukkan Baru'
        context["savebtn"] = 'Simpan'
        return context
class PengeluaranDeleteView(View):
    template_name = "delete_pengeluaran.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Pemasukkan has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        modal = get_object_or_404(Pengeluaran, pk=pk)
        return render(request, self.template_name, {'object' : modal})

    def post(self, request, pk):  
        modal = get_object_or_404(Pengeluaran, pk=pk)
        modal.is_deleted = True
        modal.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory_pengeluaran')


class PemasukkanDeleteView(View):
    template_name = "delete_pemasukkan.html"                                                 # 'delete_stock.html' used as the template
    success_message = "Pemasukkan has been deleted successfully"                             # displays message when form is submitted
    
    def get(self, request, pk):
        modal = get_object_or_404(Pemasukkan, pk=pk)
        return render(request, self.template_name, {'object' : modal})

    def post(self, request, pk):  
        modal = get_object_or_404(Pemasukkan, pk=pk)
        modal.is_deleted = True
        modal.save()                                               
        messages.success(request, self.success_message)
        return redirect('inventory_pemasukkan')