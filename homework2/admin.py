from django.contrib import admin
from .models import Human


@admin.register(Human)
class HumanAdmin(admin.ModelAdmin):
    fields = ('name', 'surname', 'gender', 'year_of_birth')
    list_display = ('name', 'surname', 'age')

    def age(self, obj):
        return 2021 - int(obj.year_of_birth)

    age.short_description = 'Age'
