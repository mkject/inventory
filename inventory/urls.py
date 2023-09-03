from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.StockListView.as_view(), name='inventory'),
    path('inventory_modal', views.ModalListView.as_view(), name='inventory_modal'),
    path('inventory_keuangan', views.keuanganListView.as_view(), name='inventory_keuangan'),
        path('inventory_pemasukkan', views.PemasukkanListView.as_view(), name='inventory_pemasukkan'),
    path('inventory_pengeluaran', views.PengeluaranListView.as_view(), name='inventory_pengeluaran'),
    path('export-excel/', views.export_excel, name='export_excel'),
    
    path('new', views.StockCreateView.as_view(), name='new-stock'),
    path('newmodal', views.ModalCreateView.as_view(), name='new-modal'),
    path('modal/<pk>/edit', views.ModalUpdateView.as_view(), name='edit-modal'),    
    path('modal/<pk>/delete', views.ModalDeleteView.as_view(), name='delete-modal'),

    path('stock/<pk>/edit', views.StockUpdateView.as_view(), name='edit-stock'),
    path('stock/<pk>/delete', views.StockDeleteView.as_view(), name='delete-stock'),

    path('newpemasukkan', views.PemasukkanCreateView.as_view(), name='new-pemasukkan'),
    path('pemasukkan/<pk>/edit', views.PemasukkanUpdateView.as_view(), name='edit-pemasukkan'),   
    path('pemasukkan/<pk>/delete', views.PemasukkanDeleteView.as_view(), name='delete-pemasukkan'), 

    path('newpengeluaran', views.PengeluaranCreateView.as_view(), name='new-pengeluaran'),
    path('pengeluaran/<pk>/edit', views.PengeluaranUpdateView.as_view(), name='edit-pengeluaran'),   
    path('pengeluaran/<pk>/delete', views.PengeluaranDeleteView.as_view(), name='delete-pengeluaran'),
]