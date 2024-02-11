from django.shortcuts import render, redirect
from .forms import MeasurementForm


def measurement_form(request):
    if request.method == 'POST':
        form = MeasurementForm(request.POST)
        if form.is_valid():
            measurement = form.save(commit=False)
            measurement.user = request.user
            measurement.save()
            return redirect('base-home')  # Create a success page
    else:
        form = MeasurementForm()

    return render(request, 'measure/measurement_form.html', {'form': form})

