from django.shortcuts import render
# from django.views.generic import TemplateView

# Create your views here.
def index(request):
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request, 'mango/index.html', context_dict)

def demo(request):
	return render(request, 'mango/demo.html')

def hello(request):
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render(request, 'mango/index.html', context_dict)
#
# class AboutView(TemplateView):
#     template_name = "demo.html"
#
# class IndexView(TemplateView):
#     template_name = "index.html"

# 404 Example
# from django.shortcuts import get_object_or_404
#
# def my_view(request):
#     my_object = get_object_or_404(MyModel, pk=1)

#