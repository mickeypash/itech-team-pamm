from django.shortcuts import render

# Create your views here.
def index(request):
	context_dict = {'boldmessage': "the start of a beautiful relationship"}
	return render(request, 'notes/index.html', context_dict)