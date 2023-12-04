from django.shortcuts import render
from datetime import date, timedelta


# Create your views here.




def programmer_day(request):
    year = date.today().year
    programmer_date = date(year, 1, 1) + timedelta(days=255)
    return render(request, 'date.html', {'programmer_date': programmer_date})