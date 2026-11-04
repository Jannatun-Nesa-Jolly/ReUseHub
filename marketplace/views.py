from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from .forms import SignUpForm, ListingForm, ReportForm
from .models import ItemListing, SavedItem, Profile


def home(request):
    listings = ItemListing.objects.filter(status=ItemListing.Status.ACTIVE).select_related('category', 'owner')
    query = request.GET.get('q', '').strip()
    category = request.GET.get('category', '')
    kind = request.GET.get('type', '')
    condition = request.GET.get('condition', '')
    if query: listings = listings.filter(Q(title__icontains=query) | Q(description__icontains=query))
    if category: listings = listings.filter(category_id=category)
    if kind: listings = listings.filter(listing_type=kind)
    if condition: listings = listings.filter(condition=condition)
    return render(request, 'marketplace/home.html', {'listings': listings, 'query': query,
        'categories': __import__('marketplace.models', fromlist=['Category']).Category.objects.all(),
        'selected_category': category, 'selected_type': kind, 'selected_condition': condition})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user, display_name=user.username)
            login(request, user)
            return redirect('home')
    else: form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required
def create_listing(request):
    form = ListingForm(request.POST or None, request.FILES or None)
    if request.method == 'POST' and form.is_valid():
        listing = form.save(commit=False); listing.owner = request.user; listing.save()
        messages.success(request, 'Your item is now listed on ReUseHub.')
        return redirect('detail', pk=listing.pk)
    return render(request, 'marketplace/listing_form.html', {'form': form, 'heading': 'Share an item'})


def detail(request, pk):
    listing = get_object_or_404(ItemListing.objects.select_related('owner', 'category'), pk=pk)
    saved = request.user.is_authenticated and SavedItem.objects.filter(user=request.user, listing=listing).exists()
    return render(request, 'marketplace/detail.html', {'listing': listing, 'saved': saved})

@login_required
def edit_listing(request, pk):
    listing = get_object_or_404(ItemListing, pk=pk, owner=request.user)
    form = ListingForm(request.POST or None, request.FILES or None, instance=listing)
    if request.method == 'POST' and form.is_valid(): form.save(); return redirect('detail', pk=pk)
    return render(request, 'marketplace/listing_form.html', {'form': form, 'heading': 'Edit item'})

@login_required
def complete_listing(request, pk):
    listing = get_object_or_404(ItemListing, pk=pk, owner=request.user)
    if request.method == 'POST': listing.status = ItemListing.Status.COMPLETED; listing.save()
    return redirect('detail', pk=pk)

@login_required
def toggle_save(request, pk):
    listing = get_object_or_404(ItemListing, pk=pk)
    saved, created = SavedItem.objects.get_or_create(user=request.user, listing=listing)
    if not created: saved.delete()
    return redirect('detail', pk=pk)

@login_required
def saved_items(request):
    items = ItemListing.objects.filter(saveditem__user=request.user).select_related('category', 'owner')
    return render(request, 'marketplace/saved.html', {'listings': items})

@login_required
def report_listing(request, pk):
    listing = get_object_or_404(ItemListing, pk=pk)
    form = ReportForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        report = form.save(commit=False); report.reporter = request.user; report.listing = listing; report.save()
        messages.success(request, 'Thanks. Your report has been sent to the admin.')
        return redirect('detail', pk=pk)
    return render(request, 'marketplace/report.html', {'form': form, 'listing': listing})
