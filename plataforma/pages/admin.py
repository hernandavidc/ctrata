from django.contrib import admin
from .models import Page, Category

class CategoryAdmin(admin.ModelAdmin):
    readonly_fields= ('created', 'updated')

class PageAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    class Media:
        css = {
            'all': ('pages/css/custom_ckeditor.css',)
        }

admin.site.register(Page, PageAdmin)
admin.site.register(Category, CategoryAdmin)
