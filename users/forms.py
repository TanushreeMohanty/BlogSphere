from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile,Post,Category,Tag

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()  # Optional email field

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'profile_picture']

class PostForm(forms.ModelForm):
    new_category = forms.CharField(
        max_length=100, required=False, help_text="Enter a new category if not listed"
    )
    new_tags = forms.CharField(
        max_length=200,
        required=False,
        help_text="Enter new tags separated by commas",
    )    
    category = forms.ModelChoiceField(queryset=Category.objects.all(), required=False, empty_label="Select a category")

    tags = forms.ModelMultipleChoiceField(queryset=Tag.objects.all(), required=False, widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ['title', 'content', 'category', 'tags']


    def clean_new_category(self):
        new_category = self.cleaned_data.get('new_category')
        if new_category:
            category, created = Category.objects.get_or_create(name=new_category)
            return category
        return None

    def clean_new_tags(self):
        new_tags = self.cleaned_data.get('new_tags')
        tag_list = []
        if new_tags:
            tag_names = [tag.strip() for tag in new_tags.split(',')]
            for name in tag_names:
                tag, created = Tag.objects.get_or_create(name=name)
                tag_list.append(tag)
        return tag_list