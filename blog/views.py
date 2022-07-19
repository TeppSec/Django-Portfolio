from django.shortcuts import render
 

# Create your views here.
def blog(request):
    # query the db to return all project objects
    #blogs = blog.objects.all()
    return render(request, 'blog_folder/index.html')