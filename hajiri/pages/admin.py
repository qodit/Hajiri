from django.contrib import admin
from pages.models import Period, Subject, Teacher, TeacherRecord


class PeriodAdmin(admin.ModelAdmin):
    pass

admin.site.register(Period, PeriodAdmin)

class TeacherRecordAdmin(admin.ModelAdmin):
    pass

admin.site.register(TeacherRecord, TeacherRecordAdmin)


class SubjectAdmin(admin.ModelAdmin):
    pass

admin.site.register(Subject, SubjectAdmin)


class TeacherAdmin(admin.ModelAdmin):
    pass

admin.site.register(Teacher, TeacherAdmin)
