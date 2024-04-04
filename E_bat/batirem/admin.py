from django.contrib import admin

# Register your models here.


from .models import *


class ImageTabularInline(admin.TabularInline):
    model = Images

class TagTabularInline(admin.TabularInline):
    model = Tag
    
class ProductAdmin(admin.ModelAdmin):
    inlines = [ImageTabularInline, TagTabularInline]
    


admin.site.register(Images)
admin.site.register(Tag)


admin.site.register(Categories)
admin.site.register(Brand)
admin.site.register(Color)
admin.site.register(Filter_Price)
admin.site.register(Product, ProductAdmin)
admin.site.register(Contact_us)



