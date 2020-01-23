from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name', 'group_id')
    list_select_related = ('group_id',)


admin.site.register(Student, StudentAdmin)
