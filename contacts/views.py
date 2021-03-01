from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError

from django.http  import HttpResponse, HttpResponseRedirect

from .forms import ContactForm
# Create your views here.
def contactView(request):
    if request.method=="POST":
        form=ContactForm()
    else:
        form=ContactForm(request.POST)
        if form.is_valid():
            email=form.cleaned_data['email']
            subjext=form.cleaned_data['subject']
            message=form.cleaned_data['message']
            try:
                send_mail(subject, message, "Obengstoney@gmail.com",[email], fail_silently=False)
            except BadHeaderError:
                return HttpResponse('Invalid header found')
            return redirect('sucesss')
    return render(request, 'contacts/contact.html', {'form': form})
def successView(request):
    return HttpResponse('Success! Thank you for your message.')


