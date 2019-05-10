from django.shortcuts import render
from django.http import HttpResponse
from .models import M1301,M1332,M1333,M1352,M1376,M1377
from .forms import HelloForm

def index(request):
#    data = M1301.objects.all()
    dekidaka_list = [] 
    takane_list = []
    owarine_list = []
    company = {}
    params = {
           'title':'Hello',
           'form':HelloForm(),
           'message':'all friends',
           'com_name':[],
           'dekidaka':[],
           'takane':[],
           'owarine':[]         
           }
    if request.method == 'POST' :
        date = request.POST['date']
        params['form'] = HelloForm(request.POST)
        for i in [M1301,M1332,M1333,M1352,M1376,M1377]:            
            rate=i.objects.filter(date = date).values_list('dekidaka', flat=True).get()/i.objects.filter(date = '2018/11').values_list('dekidaka', flat=True).get()
            company[i.__name__[1:]] = rate
            takane_list.append(i.objects.filter(date = '2018/12').values_list('top', flat=True).get())
            owarine_list.append(i.objects.filter(date = '2018/12').values_list('close', flat=True).get())
        params['com_name'] = max(company)
        params['dekidaka'] = company[max(company)]
        params['takane'] = max(takane_list)
        params['owarine'] = max(owarine_list)
    
    return render(request, 'hello/index.html', params)