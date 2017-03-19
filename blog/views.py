from django.shortcuts import render
from django.utils import timezone
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect

def main(request):
    return render(request, 'blog/main.html', {})

def post_i(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			post = form.save(commit=False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('post_they')
	else:
		form = PostForm()
	return render(request, 'blog/post_i.html', {'form': form})

def post_you(request):
    return render(request, 'blog/post_you.html', {})

def post_they(request):
    return render(request, 'blog/post_they.html', {})
