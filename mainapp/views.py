from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import *
from mainapp.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token

class MahsulotlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mahsulotlar=Mahsulot.objects.filter(sotuvchi__user=request.user)
        serializer=MahsulotSerializer(mahsulotlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        mahsulot=request.data
        serializer=MahsulotSerializer(data=mahsulot)
        if serializer.is_valid():
            serializer.save(sotuvchi=Sotuvchi.objects.get(user=request.user))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors)

class MahsulotAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        mahsulot=Mahsulot.objects.get(id=pk)
        serializer = MahsulotSerializer(mahsulot)
        if mahsulot.sotuvchi.user==request.user:
            serializer = MahsulotSerializer(mahsulot)
            return Response(serializer.data)
        return Response({"xabar": "Bu mahsulot bu userga tegishli emas!"})
    def put(self, request, pk):
        mahsulot=Mahsulot.objects.get(id=pk)
        if mahsulot.sotuvchi.user==request.user:
            serializer=MahsulotSerializer(mahsulot, data=request.data)
            if serializer.is_valid():
                serializer.save(sotuvchi=Sotuvchi.objects.get(user=request.user))
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"xabar": "Bu mahsulot bu userga tegishli emas!"})
    def delete(self, request, pk):
        mahsulot=Mahsulot.objects.get(id=pk)
        if mahsulot.sotuvchi.user==request.user:
            mahsulot.delete()
            return Response({"Success": "True"})
        return Response({"xabar": "Bu mahsulot bu sotuvchiga tegishli emas!"})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class MijozlarAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        mijozlar=Mijoz.objects.filter(sotuvchi__user=request.user)
        serializer=MijozSerializer(mijozlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        mijoz=request.data
        serializer=MijozSerializer(data=mijoz)
        if serializer.is_valid():
            serializer.save(sotuvchi=Sotuvchi.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors)

class MijozAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, pk):
        mijoz=Mijoz.objects.get(id=pk)
        serializer = MijozSerializer(mijoz)
        if mijoz.sotuvchi.user==request.user:
            serializer = MahsulotSerializer(mijoz)
            return Response(serializer.data)
        return Response({"xabar": "Bu mijoz bu userga tegishli emas!"})
    def put(self, request, pk):
        mijoz=Mijoz.objects.get(id=pk)
        if mijoz.sotuvchi.user==request.user:
            serializer=MijozSerializer(mijoz, data=request.data)
            if serializer.is_valid():
                serializer.save(sotuvchi=Sotuvchi.objects.get(user=request.user))
                return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(serializer.errors, status=status.HTTP_406_NOT_ACCEPTABLE)
        return Response({"xabar": "Bu mijoz bu userga tegishli emas!"})
    def delete(self, request, pk):
        mijoz=Mijoz.objects.get(id=pk)
        if mijoz.sotuvchi.user==request.user:
            mijoz.delete()
            return Response({"Success": "True"})
        return Response({"xabar": "Bu mijoz bu sotuvchiga tegishli emas!"})

# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class SotuvchilarAPIView(APIView):
    def get(self, request):
        sotuvchilar=Sotuvchi.objects.all()
        serializer=SotuvchiSerializer(sotuvchilar, many=True)
        return Response(serializer.data)
    def post(self, request):
        s=request.data
        serializer=UserSerializer(data=s)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)
        return Response(serializer.errors)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class StatistikalarAPIView(APIView):
    def get(self, request):
        statistikalar=Statistika.objects.filter(sotuvchi__user=request.user)
        serializer=StatistikaSerializer(statistikalar, many=True)
        return Response(serializer.data)
    def post(self, request):
        statistika=request.data
        serializer=StatistikaSerializer(data=statistika)
        if serializer.is_valid():
            serializer.save(sotuvchi=Sotuvchi.objects.get(user=request.user))
            return Response(serializer.data)
        return Response(serializer.errors)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class TokenlarAPIView(APIView):
    def get(self, request):
        tokenlar=Token.objects.all()
        serializer=TokenSerializer(tokenlar, many=True)
        return Response(serializer.data)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

class UserlarAPIView(APIView):
    def get(self, request):
        userlar=User.objects.all()
        serializer=UserSerializer(userlar, many=True)
        return Response(serializer.data)
    def post(self, request):
        user=request.data
        serializer=UserSerializer(data=user)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)

# ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


















