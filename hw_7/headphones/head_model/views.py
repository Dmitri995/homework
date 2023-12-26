from django.shortcuts import render
from django.views import View
from .models import Head_model

class Head_modelView(View):
    def get(self, request):
        model = request.GET.get('model')
        if model:
            headphones = Head_model.objects.filter(model__iexact=model).first()
            if headphones:
                return render(request, 'headphones.html', {'headphones': headphones})
        return render(request, 'not_found.html')

