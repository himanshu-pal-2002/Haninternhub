from django.shortcuts import render, redirect
from app.forms import InternshipApplicationForm
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def why_us(request):
    return render(request, 'why_us.html')

def contact(request):
    return render(request, 'contact.html')

def internship_minor(request):
    return render(request, 'internships_minor.html')

def internship_major(request):
    return render(request, 'internships_major.html')

def apply_internship(request):

    if request.method == "POST":
        form = InternshipApplicationForm(request.POST)

        if form.is_valid():
            form.save()

            messages.success(
                request,
                "Your internship application has been submitted successfully!"
            )

            return redirect('apply_internship')

    else:
        form = InternshipApplicationForm()

    return render(request, "apply_internship.html", {"form": form})
