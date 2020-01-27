from django.contrib import admin

from students.models import Student, Group


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


class StudentInline(admin.TabularInline):
    model = Student
    raw_id_fields = ('group_id',)


class GroupAdmin(admin.ModelAdmin):
    list_display = ('id', 'gr_name', 'number_of_students', 'faculty', 'department', 'starosta', 'teacher')
    list_select_related = ('starosta', 'teacher')
    inlines = [
        StudentInline,
    ]


admin.site.register(Group, GroupAdmin)
