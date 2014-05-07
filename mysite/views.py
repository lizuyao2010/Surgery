from django.shortcuts import render_to_response

def surgery_form(request):
    return render_to_response('surgery_form.html')