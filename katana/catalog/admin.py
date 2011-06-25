# -*- coding: utf-8 -*-

from django.contrib import admin
from katana.catalog.models import *

class OrganizationAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}
	search_fields = ['name']
    
class ServiceAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class LifeCycleStateAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class ProtocolAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

class CategoryAdmin(admin.ModelAdmin):
	prepopulated_fields = {'slug': ('name',)}

admin.site.register(Organization, OrganizationAdmin)
admin.site.register(ContactPerson)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Protocol, ProtocolAdmin)
admin.site.register(LifeCycleState, LifeCycleStateAdmin)
admin.site.register(Service, ServiceAdmin)
