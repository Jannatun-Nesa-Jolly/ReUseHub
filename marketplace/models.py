from django.conf import settings
from django.db import models

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    display_name = models.CharField(max_length=100, blank=True)
    contact_preference = models.CharField(max_length=150, blank=True, help_text='Optional contact detail you choose to share')
    def __str__(self): return self.display_name or self.user.username

class Category(models.Model):
    name = models.CharField(max_length=80, unique=True)
    def __str__(self): return self.name

class ItemListing(models.Model):
    class Condition(models.TextChoices):
        NEW = 'new', 'Like new'
        GOOD = 'good', 'Good'
        FAIR = 'fair', 'Fair'
    class ListingType(models.TextChoices):
        SALE = 'sale', 'For sale'
        EXCHANGE = 'exchange', 'Exchange'
        DONATION = 'donation', 'Donation'
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        COMPLETED = 'completed', 'Completed'
        ARCHIVED = 'archived', 'Archived'
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='listings')
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name='listings')
    title = models.CharField(max_length=140)
    description = models.TextField()
    condition = models.CharField(max_length=10, choices=Condition.choices)
    listing_type = models.CharField(max_length=10, choices=ListingType.choices)
    price = models.DecimalField(max_digits=9, decimal_places=2, null=True, blank=True)
    image = models.ImageField(upload_to='listings/', blank=True, null=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title

class SavedItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(ItemListing, on_delete=models.CASCADE)
    saved_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        constraints = [models.UniqueConstraint(fields=['user', 'listing'], name='unique_saved_item')]

class Report(models.Model):
    class Status(models.TextChoices):
        OPEN = 'open', 'Open'
        RESOLVED = 'resolved', 'Resolved'
    reporter = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    listing = models.ForeignKey(ItemListing, on_delete=models.CASCADE, related_name='reports')
    reason = models.TextField()
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.OPEN)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return f'Report: {self.listing.title}'
