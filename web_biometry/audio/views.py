from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.views.decorators.csrf import csrf_exempt,csrf_protect
from .forms import VoiceForm
from .models import Voice

# Create your views here.

@csrf_exempt
def index(request):
    if request.method == 'POST':
        form = VoiceForm(request.POST, request.FILES)
        print(request.FILES)
        print('Saving file...')
        voice = Voice(voice = request.FILES['voice'])
        voice.save()
        print('Saved')

        # Redirect to the document list after POST
        return HttpResponse('Test')
    return render(request, 'index.html')
