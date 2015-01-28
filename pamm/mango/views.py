from django.shortcuts import render

# Create your views here.
def index(request):
	context_dict = {'boldmessage': "I am bold font from the context"}
	return render(request, 'mango/index.html', context_dict)

# def detail(request, question_id):
#     try:
#         question = Question.objects.get(pk=question_id)
#     except Question.DoesNotExist:
#         raise Http404("Question does not exist")
#     return render(request, 'polls/detail.html', {'question': question})