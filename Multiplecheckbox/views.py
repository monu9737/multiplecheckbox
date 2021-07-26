from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def checkbox(request):
    checkbox1 = request.GET.get('checkbox1', 'off')
    checkbox2 = request.GET.get('checkbox2', 'off')
    checkbox3 = request.GET.get('checkbox3', 'off')
    checkbox4 = request.GET.get('checkbox4', 'off')

    if ((checkbox1 == "on") and (checkbox2 == "on") and (checkbox3 == "on")):
        mydict = {'text': 'checkbox1 and checkbox2 and checkbox3 is working'}
        return render(request, 'checkbox.html', mydict)
    elif ((checkbox1 == "on") and (checkbox2 == "on")):
        mydict = {'text': 'checkbox1 and checkbox2 is working'}
        return render(request, 'checkbox.html', mydict)
        # print("checkbox1 and checkbox2 is working")
        # return HttpResponse('<h1> checkbox1 and checkbox2  is working  </h1>')
    elif ((checkbox2 == "on") and (checkbox3 == "on")):
        mydict = {'text': 'checkbox2 and checkbox3 is working'}
        return render(request, 'checkbox.html', mydict)
        # print("checkbox2 and checkbox3 is working")
        # return HttpResponse('<h1> checkbox2 and checkbox3 is working  </h1>')
    elif ((checkbox3 == "on") and (checkbox1 == "on")):
        mydict = {'text': 'checkbox1 and checkbox3 is working'}
        return render(request, 'checkbox.html', mydict)
        # print("checkbox3 and checkbox1 is working")
        # return HttpResponse('<h1> checkbox3 and checkbox1 is working  </h1>')
    elif checkbox3 == "on":
        mydict = {'text': 'checkbox3 is working'}
        return render(request, 'checkbox.html', mydict)
        # print("checkbox3  is working")
        # return HttpResponse('<h1> checkbox3 is working  </h1>')
    elif checkbox2 == "on":
        mydict = {'text': 'checkbox2 is working'}
        return render(request, 'checkbox.html', mydict)
        # print("checkbox2  is working")
        # return HttpResponse('<h1> checkbox2 is working  </h1>')
    elif checkbox1 == "on":
        mydict = {'text': 'checkbox1 is working'}
        return render(request, 'checkbox.html', mydict)
        # print("checkbox1  is working")
        # return HttpResponse('<h1> checkbox1 is working  </h1>')

    else:
        return HttpResponse("error")