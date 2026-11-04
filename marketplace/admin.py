from django.contrib import admin
from .models import Profile, Category, ItemListing, SavedItem, Report
admin.site.register(Profile)
admin.site.register(Category)
@admin.register(ItemListing)
class ItemListingAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'category', 'listing_type', 'condition', 'status', 'created_at')
    list_filter = ('listing_type', 'condition', 'status', 'category')
    search_fields = ('title', 'description', 'owner__username')
@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('listing', 'reporter', 'status', 'created_at')
    list_filter = ('status',)
admin.site.register(SavedItem)
