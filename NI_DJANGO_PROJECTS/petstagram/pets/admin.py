from django.contrib import admin

# Register your models here.
from pets.models import Pet, Like


# Bellow - customisation of the admin page !!!!
# class for inlines to work - show likes with in the Pet object in admin.
class LikeInlineAdmin(admin.TabularInline):
    model = Like


# this class shows is for customisation of the pet object in the admin
class PetAdmin(admin.ModelAdmin):
    list_display = ('id', 'type', 'name', 'age')
    list_filter = ('type', 'age')
    # shows the number of likes in the pet object in admin page
    inlines = (LikeInlineAdmin,)


admin.site.register(Pet, PetAdmin)
admin.site.register(Pet)
admin.site.register(Like)
