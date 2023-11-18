from django.db import models


class BookRentalModel(models.Model):
    id = models.AutoField(primary_key=True)
    date_start = models.DateField()
    date_end = models.DateField()
    itens = models.JSONField()
    late = models.BooleanField(default=True)
    delivered = models.BooleanField()


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


class ExtendUser(models.Model):
    id = models.AutoField(primary_key=True)
    cpf = models.CharField(max_length=14)
    address = models.JSONField(default=address)
    phone1 = models.CharField(max_length=14)
    phone2 = models.CharField(max_length=14)
    phone_other1 = models.CharField(max_length=14)
    phone_other2 = models.CharField(max_length=14)
    whats = models.CharField(max_length=14)
    date_nasc = models.CharField(max_length=14)
    guardian = models.ForeignKey(GuardianModel, on_delete=models.PROTECT)


class BookPublisherModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class TypeItemModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class CategoryItensModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


class BookAuthorModel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)


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

