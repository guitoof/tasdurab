from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import ugettext_lazy as _

from users.models import User, Group
from users.forms import CustomUserChangeForm, CustomUserCreationForm

class CustomUserAdmin(UserAdmin):
    # The forms to add and change user instances

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference the removed 'username' field
    fieldsets = (
        (_('Personal informations'), {'fields': ('username', 'first_name', 'last_name', 'group')}),
        #(_('Contact'), {'fields': ('email', 'phone_number')}),
        #(_('Permissions'), {'fields': ('is_active','is_registered')}),
    )
    add_fieldsets = (
        (None, {
            #'classes': ('wide',),
            'fields': ('username', 'first_name', 'last_name')}
        ),
    )
    form = CustomUserChangeForm
    add_form = CustomUserCreationForm
    list_display = ('username', 'first_name', 'last_name')#, 'group', 'email', 'phone_number', 'building', 'room', 'is_registered', 'is_active', 'is_staff')
    list_filter = ()
    search_fields = ('username', 'email', 'first_name', 'last_name')
    ordering = ('username',)
    filter_horizontal = ()

admin.site.register(User, CustomUserAdmin)

admin.site.register(Group)
