from django.contrib import admin
from django.contrib import admin
from models import Category, Page


class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'url')

#admin.site.register(Category)
#admin.site.register(Page, PageAdmin)

# Register your models here.


# Add in this class to customized the Admin Interface
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

# Update the registeration to include this customised interface
admin.site.register(Category, CategoryAdmin)
admin.site.register(Page)



