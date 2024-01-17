from django.contrib import admin
from .models import Department,Course,Dropdown

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Department,DepartmentAdmin)


class CouseAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Course,CouseAdmin)
admin.site.register(Dropdown)




# Register your models here.
