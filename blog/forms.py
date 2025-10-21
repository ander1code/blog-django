from django import forms
from .models import Post
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    username = forms.CharField(
        label="Username",
        max_length=20,
        required=True,
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your username'
        }),
        error_messages={
            'required': 'Username is required.',
            'max_length': 'Username cannot exceed 20 characters.',
        }, 
    )
    
    password = forms.CharField(
        label="Password",
        max_length=20,
        required=True,
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter your password'
        }),
        error_messages={
            'required': 'Password is required.',
            'max_length': 'Password cannot exceed 20 characters.',
        }
    )

    def clean_username(self):
        data = self.cleaned_data["username"]
        if not data:
            raise ValidationError("Username is empty.")
        validator = RegexValidator(
            regex=r"^\S+$", 
            message="Invalid username."
        )
        validator(data)
        return data
    
    def clean_password(self):
        data = self.cleaned_data["password"]
        if not data:
            raise ValidationError("Password is empty.")
        validator = RegexValidator(
            regex=r"^\S+$", 
            message="Invalid password."
        )
        validator(data)
        return data
    

class PostForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False

    title = forms.CharField(
        max_length=70,
        error_messages={
            'required': 'Title is empty.',
            'max_length': 'Title has more than 70 characters.',
        },
        widget=forms.TextInput(attrs={
            "class":"form-control"
        })
    )

    briefing = forms.CharField(
        max_length=100,
        error_messages={
            'required': 'Briefing is empty.',
            'max_length': 'Briefing has more than 100 characters.',
        },
        widget=forms.TextInput(attrs={
            "class":"form-control"
        })
    )
    
    text = forms.CharField(
        max_length=3000,
        error_messages={
            'required': 'Text is empty.',
            'max_length': 'Text has more than 3000 characters.',
        },
        widget=forms.Textarea(attrs={
            "class":"form-control",
            "cols": 40,
            "rows": 15
        })
    )
    
    picture = forms.ImageField(
        error_messages={
            'required': 'Picture is empty.',
            'invalid': 'Invalid picture file.',
        },
        widget=forms.ClearableFileInput(attrs={
            'class': 'form-control',
        })
    )

    def clean_title(self):
        data = self.cleaned_data.get("title", "").strip()
        if not data:
            raise ValidationError("Title is empty.")
        if len(data) < 5:
            raise ValidationError("The title must contain at least 5 characters.")
        if len(data) > 70:
            raise ValidationError("The title must not exceed 70 characters.")
        return data
    
    def clean_briefing(self):
        data = self.cleaned_data.get("briefing", "").strip()
        if not data:
            raise ValidationError("Briefing is empty.")
        if len(data) < 5:
            raise ValidationError("The briefing must contain at least 5 characters.")
        if len(data) > 100:
            raise ValidationError("The briefing must not exceed 70 characters.")
        return data
    
    def clean_text(self):
        data = self.cleaned_data.get("text", "").strip()
        if not data:
            raise ValidationError("Text is empty.")
        if len(data) < 100:
            raise ValidationError("The text must contain at least 100 characters.")
        if len(data) > 3000:
            raise ValidationError("The text must not exceed 3000 characters.")
        return data
    
    def clean_picture(self):
        data = self.cleaned_data.get("picture")
        if data is None:
            raise ValidationError("Picture is empty.")

    class Meta:
        model = Post
        fields = ['title', 'briefing', 'text', 'picture']
