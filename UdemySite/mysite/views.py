from django.shortcuts import render
from django.contrib.auth.views import LoginView
from blog.models import Article

# Create your views here.
def index(request):
    objs = Article.objects.all()[:3]
    context = {
        'title': 'Really Site',
        'articles': objs,
    }
    return render(request,'mysite/index.html',context)

class Login(LoginView):
    template_name = 'mysite/login.html'
    
