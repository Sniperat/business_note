from django.contrib import admin
from .models import *


@admin.register(ProductModel)
class AddressAdmin(admin.ModelAdmin):
    def get_form(self, request, obj=None, **kwargs):
        form = super().get_form(request, obj, **kwargs)

        print(obj,'>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
        if obj == None:
            print('++++++++++++++++++++++++++++++')
            form.base_fields["size"].choices = []
            return form
        else:
            def get_true(pk) -> bool:
                if not isinstance(pk, str):
                    print(type(pk), pk.value)

                    sm = SizeModel.objects.get(id=pk.value)
                    if sm.group == obj.group:
                        return True
                return False
            form.base_fields["size"].choices = ((pk, display) for pk, display in form.base_fields["size"].choices if get_true(pk))
            return form
    list_display = ['id', 'name', 'price']
    list_display_links = ['id', 'name']
    list_filter = ('group', 'size')
    search_fields = ['name', 'price']


class StackInlineProduct(admin.StackedInline):
    model = ProductModel
    extra = 0



@admin.register(OrderModel)
class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'customer', 'phone_number','status','prepayment', 'total_price']
    list_display_links = ['id', 'customer', 'phone_number']
    list_filter = ('status', )
    search_fields = ['customer', 'phone_number']
    inlines = [StackInlineProduct]


class StackInlineSize(admin.StackedInline):
    model = SizeModel
    extra = 0

@admin.register(GroupModel)
class AddressAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', ]
    list_display_links = ['id', 'name']
    search_fields = ['name']
    inlines = [StackInlineSize, StackInlineProduct]


admin.site.register(SizeModel)