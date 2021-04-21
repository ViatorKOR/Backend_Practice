from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from ..forms import createpost
from ..models import Blog_post



def postlist(request):
    blogs = Blog_post.objects.all()
    return render(request, 'postlist.html',{'blogs':blogs})

@login_required(login_url='sign_in')
def editpost(request):
    if request.method == 'POST':
        
        form = createpost(request.POST)
        
        if form.is_valid():
            Blog_post = form.save()
            Blog_post.author = request.user
            Blog_post.save()

            return redirect('postlist')
        
        else:
            return redirect('index')
    
    else:
        form = createpost()
        return render(request, 'editpost.html',{'form': form})

def post_detail(request, blog_id):
    blog_detail = get_object_or_404(Blog_post, pk=blog_id)
    
    return render(request, 'post_detail.html' ,{'blog_detail':blog_detail})
