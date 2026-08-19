from django import forms
from .models import InternshipApplication
import re


class InternshipApplicationForm(forms.ModelForm):

    class Meta:
        model = InternshipApplication
        fields = "__all__"

        widgets = {
            'title_of_internship': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter internship title'
            }),

            'student_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter your full name'
            }),

            'registration_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter registration number'
            }),

            'course': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'BCA / MCA / BSc'
            }),

            'specialization': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'AI / Data Science / Web Development'
            }),

            'year': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1 - 4'
            }),

            'semester': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': '1 - 8'
            }),

            'college': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter college name'
            }),

            'university_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter university name'
            }),

            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter email address'
            }),

            'contact_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter 10 digit mobile number'
            }),
        }

    # Mobile number validation
    def clean_contact_number(self):

        contact = self.cleaned_data.get("contact_number")

        if not contact:
            return contact

        if not re.match(r'^[6-9]\d{9}$', contact):
            raise forms.ValidationError(
                "Enter a valid 10 digit mobile number starting with 6,7,8 or 9"
            )

        if InternshipApplication.objects.filter(contact_number=contact).exists():
            raise forms.ValidationError(
                "This mobile number has already applied."
            )

        return contact


    # Email validation
    def clean_email(self):

        email = self.cleaned_data.get("email")

        if email and InternshipApplication.objects.filter(email=email).exists():
            raise forms.ValidationError(
                "This email already exists."
            )

        return email


    # Registration validation
    def clean_registration_number(self):

        reg = self.cleaned_data.get("registration_number")

        if reg and InternshipApplication.objects.filter(registration_number=reg).exists():
            raise forms.ValidationError(
                "This registration number already exists."
            )

        return reg


    # Prevent applying twice for same internship
    def clean(self):

        cleaned_data = super().clean()

        reg = cleaned_data.get("registration_number")
        internship = cleaned_data.get("title_of_internship")

        if reg and internship:

            if InternshipApplication.objects.filter(
                registration_number=reg,
                title_of_internship=internship
            ).exists():

                raise forms.ValidationError(
                    "You have already applied for this internship."
                )

        return cleaned_data