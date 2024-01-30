from django.db import models
from django.contrib.auth.models import User


def user():
    r = {
        'id': '',
        'nome': '',
        'cpf': '',
        'address': address(),
        'phone1': '',
        'phone2': '',
        'phone_other1': '',
        'phone_other2': '',
        'whats': '',
        'date_nasc': '',
        'guardian': {
            'id': '',
            'name': '',
            'cpf': '',
            'address': address(),
        }
    }


class BookRentalModel(models.Model):
    id = models.AutoField(primary_key=True)
    date_start = models.DateField()
    date_end = models.DateField()
    itens = models.JSONField()
    late = models.BooleanField(default=True)
    delivered = models.BooleanField()
    client = models.JSONField(null=True)

    class Meta:
        verbose_name = 'Aluguel'
        verbose_name_plural = 'Alugueis'


def address():
    r = {
        'street': '',
        'city': '',
        'disctric': '',
        'number': '',
        'country': '',
    }
    return r


class GuardianModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    cpf = models.CharField(max_length=14)
    address = models.JSONField(default=address)
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14)
    email = models.EmailField()
    whats = models.CharField(max_length=14)
    date_nasc = models.CharField(max_length=14)

    class Meta:
        verbose_name = 'Responsável'
        verbose_name_plural = 'Responsáveis'


class ExtendUser(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14)
    address = models.JSONField(default=address)
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14)
    phone_other1 = models.CharField(max_length=14)
    phone_other2 = models.CharField(max_length=14)
    whats = models.CharField(max_length=14)
    date_nasc = models.DateField()
    guardian = models.ForeignKey(GuardianModel, on_delete=models.PROTECT, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None, null=True)


class BookPublisherModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Editora'
        verbose_name_plural = 'Editoras'


class TypeItemModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Tipo'
        verbose_name_plural = 'Tipos'


class CategoryItensModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'


class BookAuthorModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Author'
        verbose_name_plural = 'Autores'


class ItensModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    category = models.ForeignKey(CategoryItensModel, on_delete=models.PROTECT)
    plusher = models.ForeignKey(BookPublisherModel, on_delete=models.PROTECT)
    author = models.ForeignKey(BookAuthorModel, on_delete=models.PROTECT)
    year_publish = models.DateField()
    version = models.IntegerField()
    count = models.IntegerField()
    obs = models.TextField()

    class Meta:
        verbose_name = 'Item'
        verbose_name_plural = 'Itens'
