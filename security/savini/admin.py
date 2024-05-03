from django.contrib import admin

from .models import UserData

from .models import Contact

class passwordsAdmin(admin.ModelAdmin):
    readonly_fields = ('user','app_name','password')

admin.site.register(UserData, passwordsAdmin)

admin.site.register(Contact)