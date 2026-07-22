from webbrowser import register

from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from to_mes.services.from_mes.mold import specification,weekcard,mold_status,stop_status,stop_report
from django.http import HttpResponse
from to_mes.services.from_mes.stock import get_correspondence_dict, get_stock_show

#----登录
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view
from rest_framework.response import Response
#--------

def index(request):
    return HttpResponse("Hello Machine")



from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Correspondence,Stock
from .serializers import CorrespondenceSerializer,StockSerializer

from rest_framework.views import APIView


class Specification(APIView):
    def get (self, request, ):
        factory=request.query_params.get('factory','1')
        data=specification(factory)
        return Response(data)

class WeekCard(APIView):
    def post(self,request):
        body=request.data
        res=weekcard(body)
        return Response(res)
        return Response(res)
class MoldStatus(APIView):
    def post(self,request):
        body=request.data
        res=mold_status(body)
        return Response(res)
class StopReport(APIView):
    def post(self,request):
        body=request.data
        res=stop_report(body)
        return Response(res)
class StopStatus(APIView):
    def post(self,request):
        body=request.data
        res=stop_status(body)
        repr(res)
        print(res)

        return Response(res)
class StockShow(APIView):
    def post(self,request):
        body=request.data
        res=stock_show(body)
        return Response(res)


@api_view(["POST"])
def stock_show(request):
    factory=request.data.get("factory","1")
    factory=str(factory)
    print(factory)

    show=get_stock_show(factory)



    return Response(show)

#------------------------------------------------
class StockViewSet(ModelViewSet):
    queryset = Stock.objects.all()
    serializer_class = StockSerializer


class StockCorViewSet(ModelViewSet):
    queryset = Correspondence.objects.all()
    serializer_class = CorrespondenceSerializer

#--------登录界面------

from django.http import JsonResponse
from django.views.decorators.csrf import ensure_csrf_cookie

@ensure_csrf_cookie
def csrf(request):
    return JsonResponse({"code": 200})

from rest_framework.permissions import IsAuthenticated

class Me(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "code": 200,
            "username": request.user.username
        })



class LoginView(APIView):

    def post(self, request):

        username = request.data.get("username")
        password = request.data.get("password")

        user = authenticate(
            username=username,
            password=password
        )

        if user:
            login(request._request, user)

            return Response({
                "code": 200,
                "msg": "登录成功"
            })

        return Response({
            "code": 400,
            "msg": "用户名或密码错误"
        })

