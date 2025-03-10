from django.contrib import admin
from .models import Profile, Post, Category, Tag

# Profile Admin
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'bio', 'profile_picture')
    search_fields = ('user__username', 'bio')

# Post Admin
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'category', 'created_at')
    search_fields = ('title', 'content', 'author__username', 'category__name')
    list_filter = ('created_at', 'author', 'category', 'tags')
    ordering = ('-created_at',)
    filter_horizontal = ('tags',)  # Allows easy tag selection

# Category Admin
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

# Tag Admin
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
