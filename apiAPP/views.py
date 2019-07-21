from django.shortcuts import render,HttpResponse,redirect
from apiAPP import models
from django.db.models import F,Q
from apiAPP import views
from django.views import View
from utils import form_class
from utils.bin import run
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
import json
# Create your views here.

class List(View):
    def get(self,request,*args,**kwargs):
        host_list=models.Host.objects.all().order_by("id") #需要进行排序
        print(host_list)
        #分页,表示一页显示三条数据
        p = Paginator(host_list,4)
        get_page=int(request.GET.get('page',1))
        try:
            host_list=p.page(get_page)
        except PageNotAnInteger:
            host_list=p.page(1)
        except EmptyPage:
            host_list=p.page(p.num_pages)
        return render(request,'host.html',locals())

    def post(self,request,*args,**kwargs):
        pass
class Add(View):
    '''基于form的增加'''
    def post(self,request,*args,**kwargs):
        form = form_class.HostForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            models.Host.objects.create(**form.cleaned_data)
            print('提交正常')
            return redirect('/api/list')
        else:
            print(form.errors)
            return render(request,'add.html',locals())
    def get(self,request,*args,**kwargs):
        form = form_class.HostForm()
        return render(request,'add.html',locals())

class Update(View):
    def post(self,request,pk):
        print("post-id: %s" %pk)
        form = form_class.HostForm(data=request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            models.Host.objects.filter(id=pk).update(**form.cleaned_data)
            print('提交正常')
            return redirect('../list')
        else:
            print(form.errors)
            return render(request,'edit.html',locals())
    def get(self,request,pk):
        print('get_id: %s' %pk)
        obj = models.Host.objects.filter(id=pk).first()
        print (obj)
        form = form_class.HostForm(
            initial={
                'hostname':obj.hostname,
                'cpu':obj.cpu,
                'mem':obj.mem,
                'speed':obj.speed,
                'eth0_network': obj.eth0_network,
                'source_id': obj.source_id,
                'region_id': obj.region_id,
                'state': obj.state,
                #'get_state_display ':obj.get_state_display
            }
        )
        return render(request,'edit.html',locals())

class Del(View):
    def post(self,request,*args,**kwargs):
        pass
    def get(self,request,*args,**kwargs):
        get_id=int(request.GET.get('id'))
        models.Host.objects.filter(id=get_id).delete()
        print('正常删除')
        return redirect('list.html')


# class Apilist(View):
#
#         def get(self,request):
#             print("GET")
#             print(request.GET)
#             return HttpResponse("api 调用成功！")
#         def post(self, request):
#             print("POST")
#             print(request.POST)
#             return HttpResponse("api 调用成功！")

