from django.contrib import admin
from .models import Post
# Register your models here.


#admin.site.register(Post)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title','author','status','publish','created','updated']
    list_filter =  ['author','status']
    prepopulated_fields = {'slug':('title',)}
    #raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status','publish']
