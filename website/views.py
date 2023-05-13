from django.shortcuts import render, HttpResponse, redirect
from django.core.mail import send_mail
from django.core.files.storage import FileSystemStorage



from .forms import *
from .models import *


def home(request):
    if request.method == "POST":
        merk = request.POST['merk']
        year = request.POST['year']
        transmission = request.POST['transmission']
        nrg = request.POST['nrg']
        km = request.POST['km']
        price = request.POST['price']
        desc = request.POST['desc']
        email = request.POST['email']
        file = request.POST['file']
        naam = request.POST['naam']
        voornaam = request.POST['voornaam']
        gsm = request.POST['gsm']

        # groupement

        car_data = "Merk: " + merk + "\n" "Jaar: " + year + "\n""Transmissie: " \
                   + transmission + "\n""Brandstof: " + nrg + "\n""Kilometres: " + km + "\n""Prijs: " \
                   + price + "\n" "Description: " + desc + "\n""Email: " + email + "\n""Photos: " \
                   + file + "\n" "Naam: " + naam + "\n""Voornaam: " + voornaam + "\n""GSM nummer: " + gsm

        # send an email from form
        send_mail(
            'Taha, message from' + voornaam,  # subject
            car_data,  # message
            email,  # from email
            ['exportcar@outlook.be']  # to email
        )

        return render(request, 'home.html', {'merk': merk, 'year': year,
                                             'transmission': transmission,
                                             'nrg': nrg, 'km': km, 'price': price,
                                             'desc': desc, 'email': email,
                                             'file': file, 'naam': naam,
                                             'voornaam': voornaam, 'gsm': gsm, })
    else:
        return render(request, 'home.html', {})


# contact page

def contact(request):
    return render(request, 'contact.html', {})


# about page

def about(request):
    return render(request, 'about.html', {})


# form data

def form_data(request):
    form = Car_dataForm()

    data = {
        'form': form,

    }
    return render(request, 'upload.html', data)


# upload file
def upload(request):
    if request.method == 'POST':
        form = Car_dataForm(request.POST, request.FILES or None)
        if form.is_valid():
            form.save()
            subject = "Таха новая машина пришла"
            body = {
                'mark': form.cleaned_data['mark'],
                'year': form.cleaned_data['year'],
                'nrg': form.cleaned_data['nrg'],
                'transmission': form.cleaned_data['transmission'],
                'km': form.cleaned_data['km'],
                'price': form.cleaned_data['price'],
                'message': form.cleaned_data['description'],
                'email': form.cleaned_data['email'],
                'name': form.cleaned_data['name'],
                'tel': form.cleaned_data['tel'],
                'photo': form.cleaned_data['photo']

            }
            message = "\n".join(map(str, body.values()))
            send_mail(subject, message, 'exportcar@outlook.be', ['exportcar@outlook.be'])
            return render(request, 'thanks.html')

    form = Car_dataForm()

    data = {
        'form': form,
    }
    return render(request, 'upload.html', data)


from django.views.generic.edit import FormView
from .forms import FileFieldForm

class FileFieldView(FormView):
    form_class = FileFieldForm
    template_name = 'upload.html'  # Replace with your template.
    success_url = '...'  # Replace with your URL or reverse().

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                f.save()  # Do something with each file.
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

def thanks(request):
    return render(request, 'thanks.html', {})


# Upload multiple files 


from django.shortcuts import render






from django.views.generic.edit import FormView
from .forms import UploadForm
from .models import Attachment

class UploadView(FormView):
    template_name = 'form.html'
    form_class = UploadForm
    success_url = '/done/'

    def form_valid(self, form):
        for each in form.cleaned_data['attachments']:
            Attachment.objects.create(file=each)
        return super(UploadView, self).form_valid(form)