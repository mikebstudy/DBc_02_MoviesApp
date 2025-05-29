from django.shortcuts import render, HttpResponse

# Create your views here.
def index(request):
    '''
    Home test page
    '''
    #return HttpResponse("Movies!")
    return render(request, 'movies/index.html', { "movies": ["galdiator", "top gun", "shockwell"]})


def about(request):
    '''
    About page
    '''
    return render(request, 'movies/about.html', {})