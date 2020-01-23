from django.contrib import admin

from students.models import Student


class StudentAdmin(admin.ModelAdmin):
    # readonly_fields = ('email', 'telephone')
    list_display = ('id', 'first_name', 'last_name', 'group_id')
    list_select_related = ('group_id',)
    list_per_page = 10

    def get_readonly_fields(self, request, obj=None):
        if request.user.groups.filter(name='manager').exists():
            return ('email', 'telephone')
        return ()



admin.site.register(Student, StudentAdmin)
