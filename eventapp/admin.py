from django.contrib import admin
from eventapp.models import User

class UserAdmin(admin.ModelAdmin):
	fields = ['first_name' ,'email','password', 'last_name','username','mobil']


admin.site.register(User,UserAdmin)

# from eventregistry.models import Registration




# class AdminRegistration(admin.ModelAdmin):

#    fields = ['user_name','password']




# admin.site.register(Registration,AdminRegistration)