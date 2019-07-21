from app.utils import auth
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from apiAPP import models
import json
from django.http import JsonResponse

'''
    oldboy
'''
class AssetView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(AssetView, self).dispatch(request, *args, **kwargs)
    #用装饰器完成认证
    @method_decorator(auth.api_auth)
    def get(self,request,*args,**kwargs):
        """
         获取今日未更新的资产 - 适用SSH或Salt客户端
        :param request:
        :param args:
        :param kwargs:
        :return:
        """
        # response = asset.get_untreated_servers()
        # return JsonResponse(response.__dict__)
        pass

    @method_decorator(auth.api_auth)
    def post(self,request,*args,**kwargs):
        server_info = json.loads(request.body.decode('utf-8'))
        server_info = json.loads(server_info)
        hostname = server_info['hostname']
        ret = {'code':1000,'message':'[%s]更新完成' %hostname}
        #更新资产入库
        server_obj = models.Server.objects.filter(hostname=hostname).select_related('asset').first()
        if not server_obj:
            ret['code'] = 1002
            ret['message'] = '[%s]资产不存在' % hostname
            return JsonResponse(ret)