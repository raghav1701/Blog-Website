from django.shortcuts import render
from posts.models import post
from posts.models import testing
from marketing.models import newsletter


def index(request):
	queryset = post.objects.filter(featured=True)
	latest = post.objects.order_by('-timestamp')[0:3]
	my_form = testing() 
	if request.method == "POST":
		my_form = testing(request.POST) # it does the validation of all the fields required that we put in our class
		if my_form.is_valid():
			#now the data is clean
			print(my_form.cleaned_data)
			newsletter.objects.create(**my_form.cleaned_data)
	context ={
		'object_list': queryset,
		'latest': latest,
		'form' : my_form
	}
	 
	
	
	return render(request, "index.html", context)


def blog(request):
	return render(request, 'blog.html', {})


def postss(request):
	return render(request, 'post.html', {})

  