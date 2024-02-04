from django.shortcuts import render, get_object_or_404, redirect
from .models import Restaurant

from .forms import RestaurantForm

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    return render(request, template_name='restaurant_list.html', context={'restaurants': restaurants})


def restaurant_delete(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    if request.method == 'POST':
        restaurant.delete()
        return redirect('restaurant_list')
    return render(request, template_name='restaurant_confirm_delete.html', context={'restaurant': restaurant})


def restaurant_edit(request, id):
    restaurant = get_object_or_404(Restaurant, id=id)
    form = RestaurantForm(instance=restaurant)
    if request.method == 'POST':
        form = RestaurantForm(request.POST, instance=restaurant)
        if form.is_valid():
            form.save()
            return redirect('restaurant_list')
    return render(request, template_name='restaurant_edit.html', context={'form': form})



def restaurant_search(request):
    query = request.GET.get('query')
    restaurants = Restaurant.objects.filter(specialization__icontains=query)
    return render(request, template_name='restaurant_search.html', context={'restaurants': restaurants})


def restaurants():
    return None


