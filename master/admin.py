from django.contrib import admin

# Register your models here.
from .models import User
from .models import Division
from .models import Content

admin.site.register(User)
admin.site.register(Division)
admin.site.register(Content)
