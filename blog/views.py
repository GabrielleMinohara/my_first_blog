from django.shortcuts import render
<<<<<<< HEAD
=======
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm

>>>>>>> parent of 14887a1... Versão final

# Create your views here.
def post_list(request):
    return render(request, 'blog/post_list.html.txt', {})
