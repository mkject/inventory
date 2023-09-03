from django.db import models
    
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name
class Modal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)

    def __str__(self):
	    return self.name
class Pengeluaran(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    tanggal = models.DateTimeField(auto_now=True)
    
    def __str__(self):
	    return self.name
class Pemasukkan(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=0)
    is_deleted = models.BooleanField(default=False)
    tanggal = models.DateTimeField(auto_now=True)
    
    def __str__(self):
	    return self.name
class Keuangan(models.Model):
    id = models.AutoField(primary_key=True)
    keterangan = models.CharField(max_length=22, unique=True)
    jenisKeuangan = models.CharField(max_length=6, unique=False)
    Nominal = models.IntegerField(default=0)

    def __str__(self):
	    return self.keterangan