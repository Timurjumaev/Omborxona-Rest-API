from rest_framework.exceptions import ValidationError
from .models import *
from rest_framework.serializers import ModelSerializer
from rest_framework.authtoken.models import Token

class TokenSerializer(ModelSerializer):
    class Meta:
        model=Token
        fields='__all__'

class SotuvchiSerializer(ModelSerializer):
    class Meta:
        model=Sotuvchi
        fields= '__all__'

class MahsulotSerializer(ModelSerializer):
    class Meta:
        model=Mahsulot
        fields= '__all__'

class MijozSerializer(ModelSerializer):
    class Meta:
        model=Mijoz
        fields= '__all__'
    def validate_qarz(self, qiymat):
        if qiymat>500000:
            raise ValidationError("Mijozda bunday katta qarz bo'lishi mimkin emas!")
        return qiymat

class StatistikaSerializer(ModelSerializer):
    class Meta:
        model=Statistika
        fields= '__all__'

class UserSerializer(ModelSerializer):
    class Meta:
        model=User
        fields=["id", "username", "password"]

    def create(self, validated_data):
        user = User(
            username=validated_data['username']
        )
        user.set_password(validated_data['password'])
        user.save()
        return user