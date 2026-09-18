from django.shortcuts import render, redirect
from .forms import ReferralApplicationForm


def referral(request):
    if request.method == 'POST':
        form = ReferralApplicationForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            return redirect('referral_success')

    else:
        form = ReferralApplicationForm()

    return render(request, 'referral/referral.html', {'form': form})


def referral_success(request):
    return render(request, 'referral/success.html')