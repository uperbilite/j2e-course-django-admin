from django.contrib import admin

from .models import Book
from .models import User
from .models import Item

admin.site.register(Book)
admin.site.register(User)
admin.site.register(Item)
