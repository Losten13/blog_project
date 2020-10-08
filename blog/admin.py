from django.contrib import admin

# Register your models here.
from blog.models import Snippet

admin.site.register(Snippet)
