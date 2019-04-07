from django.contrib import admin
from .models import Company, Advertisement, Comment, CompanyFavorite, AdFavorite

admin.site.register(Company)
admin.site.register(Advertisement)
admin.site.register(Comment)
admin.site.register(CompanyFavorite)
admin.site.register(AdFavorite)
