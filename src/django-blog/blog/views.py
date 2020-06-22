from django.shortcuts import render
# Create your views here.

posts = [
	{
		'author': 'Navroop Singh',
		'title': 'Blog Post 1',
		'content': 'First Post',
		'date_posted': '2020-05-29'
	},
		{
		'author': 'John Doe',
		'title': 'Blog Post 2',
		'content': 'Second Post',
		'date_posted': '2020-05-30'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

def about(request):
	return render(request, 'blog/about.html', {'title': 'About'})
