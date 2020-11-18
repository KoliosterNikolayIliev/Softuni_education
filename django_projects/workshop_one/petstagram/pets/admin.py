from django.contrib import admin

# Register your models here.
from pets.models import Like, Pet


class PetAdmin(admin.ModelAdmin):
    # fields = ('type', 'name')
    list_display = ('type', 'name')
    list_filter = ('type','age')


admin.site.register(Pet, PetAdmin)
admin.site.register(Like)
