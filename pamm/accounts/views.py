from django.shortcuts import render

# Create your views here.
def login(request):

    if request.method == 'POST':
        username = request.POST.get('username', None)
        password = request.POST.get('password', None)

        auth = authenticate(username=username, password=password)
        if auth is not None:
            login(request, auth)
            return HttpResponseRedirect(reverse('notes:index'))
        else:
            messages.add_message(request, messages.INFO, "Authentication failed :(")
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'home.html')