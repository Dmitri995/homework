from django.shortcuts import render

# Create your views here.



def multiplication_table(request):
    numbers = range(1, 11)
    table = []
    for i in numbers:
        row = []
        for j in numbers:
            row.append(i * j)
        table.append(row)
    return render(request, 'table.html', {'table': table})
