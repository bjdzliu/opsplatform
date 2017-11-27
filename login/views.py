from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth import authenticate, login


import json

# Create your views here.
def userlogin(request):
    if request.method == 'POST':
        # received_json_data = json.loads(request.body)
        # for k,v in received_json_data.item():
        #     print(k,v)
        # 默认的form post提交过来的数据获取方式
         a = request.POST['username']
         b = request.POST['password']
         print(a,b)
         user = authenticate(username=a, password=b)
         if user:
             login(request, user)
             # return render(request, 'index.html')
             return HttpResponseRedirect(reverse('index'))
         else:
             return HttpResponse("sorry")
    if request.method == 'GET':
        return render(request,'login.html')

def index(request):
    return render(request, 'index.html')