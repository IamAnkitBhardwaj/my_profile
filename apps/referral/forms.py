from django import forms
from .models import ReferralApplication


class ReferralApplicationForm(forms.ModelForm):
    class Meta:
        model = ReferralApplication
        fields = [
            'full_name',
            'email',
            'phone',
            'qualification',
            'graduation_year',
            'experience',
            'skills',
            'preferred_location',
            'linkedin',
            'github',
            'resume',
            'message',
        ]

        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name',
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your email address',
            }),

            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your phone number',
            }),

            'qualification': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. BCA, B.Tech, MCA',
            }),

            'graduation_year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2026',
            }),

            'experience': forms.Select(attrs={
                'class': 'form-select',
            }),
            'experience_years': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. 2',
            }),
            'current_company_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Google, Microsoft, Amazon',
            }),
            'skills': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 3,
                'placeholder': 'Python, SQL, Java, etc.',
            }),

            'preferred_location': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'e.g. Noida, Delhi, Bangalore',
            }),

            'linkedin': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://linkedin.com/in/your-profile',
            }),

            'github': forms.URLInput(attrs={
                'class': 'form-control',
                'placeholder': 'https://github.com/your-profile',
            }),

            'resume': forms.ClearableFileInput(attrs={
                'class': 'form-control',
            }),

            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Anything you would like to share...',
            }),
        }