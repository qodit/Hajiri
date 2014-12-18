from django.contrib import admin
from pages.models import Period, Subject, Teacher, TeacherRecord, Record, Student


class PeriodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Period, PeriodAdmin)

class StudentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Student, StudentAdmin)

class RecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(Record, RecordAdmin)


class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)
