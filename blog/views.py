from django.shortcuts import render
from django.shortcuts import HttpResponse
from blog import models

# Create your views here.

# user_list = [
#     {"user": "jack", "pwd": "abc"},
#     {"user": "tom", "pwd": "ABC"},
# ]


def index(request):
    if request.method == "POST":
        username = request.POST.get("username", None)
        password = request.POST.get("password", None)
        # print(username, password)
        # temp = {"user": username, "pwd": password}
        # user_list.append(temp)
        # 添加数据到数据库
        models.UserInfo.objects.create(user=username, pwd=password)
    # 从数据库中读取所有数据
    user_list = models.UserInfo.objects.all()
        
    # return HttpResponse('hello world!')
    # return render(request, 'index.html',)
    return render(request, 'index.html', {"data": user_list})


