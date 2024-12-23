from django.contrib import admin

# Register your models here.  
from app.models import *

admin.site.register(Parent) 
admin.site.register(Child)
