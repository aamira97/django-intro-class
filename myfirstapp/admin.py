from django.contrib import admin
from .models import Person

# admin.site.register(Person)


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name')
#     list_display = ('first_name', 'last_name')

@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ('upper_case_name',)

    def upper_case_name(self, obj):
        return (obj.first_name + ' ' + obj.last_name).upper()

    upper_case_name.short_description = 'Name'










# admin.site.register(Person)


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     fields = ('first_name',)


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     fields = ('first_name', 'last_name')
#     list_display = ('first_name', 'last_name')


# @admin.register(Person)
# class PersonAdmin(admin.ModelAdmin):
#     list_display = ('upper_case_name',)
#
#     def upper_case_name(self, obj):
#         return (obj.first_name + ' ' + obj.last_name).upper()
#
#     upper_case_name.short_description = 'Name'
