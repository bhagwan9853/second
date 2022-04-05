from django.contrib import admin

from .models import *

# Register your models here.
admin.site.register([Books, Issued, Person,User])
admin.site.site_header="Bk Libray Management",
admin.site.site_title="Libray Management"