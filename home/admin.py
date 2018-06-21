from django.contrib import admin
from home.models import *

class Admin_User(admin.ModelAdmin):
    list_display =['firstName','lastName','emailId']


class  Admin_Item(admin.ModelAdmin):
     list_display = ['name','user','price','image_tag']


admin.site.register(Item,Admin_Item)
admin.site.register(User,Admin_User)
