from django.shortcuts import render

from goods.models import Products


# Create your views here.
def index(request):
    
    goods = Products.objects.all()
    
    context = {
        'title':'Home',
        'goods': goods,
    }
    
    return render(request, 'main/index.html', context=context)
    
