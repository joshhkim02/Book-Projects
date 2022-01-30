# username: 11_admin
# password: you know what it is

from django.contrib import admin

from .models import Topic, Entry

# Register your models here.
admin.site.register(Topic)
admin.site.register(Entry)

