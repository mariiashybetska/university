from django.contrib import admin

from teachers.models import Teacher


class TeacherAdmin(admin.ModelAdmin):
    list_per_page = 25

    def get_list_display(self, request, obj=None):
        if request.user.groups.filter(name='manager').exists():
            return ('id', 'full_name', 'faculty', 'email')
        return ('id', 'full_name', 'birth_date', 'email', 'telephone', 'faculty')


admin.site.register(Teacher, TeacherAdmin)
