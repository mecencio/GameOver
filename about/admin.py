from django.contrib import admin
from about.models import cancelRequest, messagesContactUs

# Register your models here.

admin.site.register(cancelRequest)

admin.site.register(messagesContactUs)
