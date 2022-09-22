from django.contrib import admin
from . models import (Blog)
from . models import (Review)

#Zona donde registro los modelos en mi admin estos me sirven como tablas de una bd
@admin.register(Blog) 
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','name','is_active')
    readonly_fields = ('slug',)

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('name','description','body')
