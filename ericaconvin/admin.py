from django.contrib import admin
from .models import Restaurant
from .models import Category
from .models import Facilities

admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Facilities)