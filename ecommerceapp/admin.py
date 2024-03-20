from django.contrib import admin
from ecommerceapp.models import  Contact,Product,Orders,OrderUpdate,Prescribed_Medicine,PrescribedProduct
# Register your models here.
admin.site.register(Contact)
admin.site.register(Product)
admin.site.register(Orders)
admin.site.register(OrderUpdate)
admin.site.register(PrescribedProduct)

@admin.register(Prescribed_Medicine)
class Prescribed_MedicineModelAdmin(admin.ModelAdmin):
    list_display = ['prescribed_status', 'id', 'user', 'product', 'photo', 'date']