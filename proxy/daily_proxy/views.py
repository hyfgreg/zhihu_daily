import json

import requests
from django.conf import settings
# from rest_framework.response import Response
from django.http.response import JsonResponse, HttpResponse
from django.views import generic
from rest_framework.views import APIView
# from common_rest.views import CustomizedAPIView, expose


# Create your views here.

class API_Proxy(APIView):
    def get(self, request,param):
        # param = request.parser_context['kwargs']['param']
        url = '{}{}'.format(settings.API_PATH, param)
        resp = requests.get(url, headers=settings.HEADERS)
        if resp.status_code // 100 == 2:
            return JsonResponse(data=json.loads(resp.text))
        else:
            return JsonResponse(status=404, data={'result': None})



class IMG_Proxy(APIView):
    def get(self, request):
        try:
            img = request.query_params['img']
            # url = '{}{}'.format(settings.API_PATH, param)
            # print(param)
            url = img
            resp = requests.get(url, headers=settings.HEADERS)
            if resp.status_code // 100 == 2:
                return HttpResponse(content=resp.content, content_type=resp.headers['Content-Type'])
            else:
                return JsonResponse(status=404, data={'result': None})
        except Exception as exc:
            return JsonResponse(status=404,data={'result':str(exc)})

    def post(self, request):
        data = request.data
        try:
            img = data['img']
            resp = requests.get(img, headers=settings.HEADERS)
            if resp.status_code // 100 == 2:
                return HttpResponse(content=resp.content, content_type=resp.headers['Content-Type'])
            else:
                return JsonResponse(status=404, data={'result': None})
        except Exception as exc:
            return JsonResponse(status=404, data={'result': str(exc)})
