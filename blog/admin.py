from django.contrib import admin
from .models import Category,Post

# configration of category model
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('imageTag','title','url','addDate')
    search_fields = ('title','addDate')

# configration of post model
class PostAdmin(admin.ModelAdmin):
    list_display = ('title','url','image','cat')
    search_fields = ('title',)
    list_filter = ('cat',)
    list_per_page = 50

admin.site.register(Category,CategoryAdmin)
admin.site.register(Post,PostAdmin)
