from django.contrib import admin
from api.models import *
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


class BookRentalAdmin(admin.ModelAdmin):
    list_display = ['date_start', 'date_end', 'itens', 'late', 'delivered', 'client']


class GuardianAdmin(admin.ModelAdmin):
    list_display = ['name', 'cpf', 'address', 'phone1', 'phone2', 'email', 'whats', 'date_nasc']


class EmployeeInLine(admin.StackedInline):
    model = ExtendUser
    can_delete = False
    verbose_name_plural = 'ExtendUser'


class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInLine,)


class BookPublisherAdmin(admin.ModelAdmin):
    list_display = ['name']


class TypeItemAdmin(admin.ModelAdmin):
    list_display = ['name']


class CategoryItensAdmin(admin.ModelAdmin):
    list_display = ['name']


class BookAuthorAdmin(admin.ModelAdmin):
    list_display = ['name']


class ItensAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(BookRentalModel, BookRentalAdmin)
admin.site.register(GuardianModel, GuardianAdmin)
admin.site.register(BookPublisherModel, BookPublisherAdmin)
admin.site.register(TypeItemModel, TypeItemAdmin)
admin.site.register(CategoryItensModel, CategoryItensAdmin)
admin.site.register(BookAuthorModel, BookAuthorAdmin)
admin.site.register(ItensModel, ItensAdmin)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
