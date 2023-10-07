from django.shortcuts import render, redirect
from .models import Item
from .forms import ItemForm

# Create your views here.


def get_todo_list(request):
    context = {
        'items': Item.objects.all()
    }
    return render(request, 'todo/todo_list.html', context)

def add_item(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        if form.is_valid():
            # save the form
            form.save()
            return redirect('get_todo_list')
        else:
            print('form is not valid')
        
    form = ItemForm()
    context = {
        'form': form
    }


    return render(request, 'todo/add_item.html', context)