from unittest import TestCase

from rest_framework.authtoken.models import Token
from rest_framework.test import APIClient

from mainapp.models import *
from mainapp.serializers import *

class TestUsersView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()

    def test_hamma_userlar(self):
        natija = self.client.get('/userlar/')
        assert natija.status_code == 200
        # assert len(natija.data) == 4
        # assert dict(natija.data[0])['username'] == 'u'


class TestMahsulotlarView(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        token = Token.objects.get(user__username='user1')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_hamma_mahsulotlar(self):
        natija = self.client.get('/mahsulotlar/')
        assert natija.status_code == 200
        # self.assertEqual(len(natija.data), 3)
        # self.assertEqual(dict(natija.data[0])['nom'], 'Coca-Cola')

    def test_mahsulot_qoshish(self):
        mahsulot = {"id": 1,"nom": "nomm1","narx": 1,"miqdor": 1,"brend": "brendd1","kelgan_sana": "2022-11-16","olchov": "olchov1","sotuvchi": 1}
        natija = self.client.post('/mahsulotlar/', data=mahsulot, format='json')
        assert natija.status_code == 201
        assert natija.data['id'] is not None
        assert natija.data['id'] == Mahsulot.objects.last().id
        assert natija.data['nom'] == 'nomm1'
        assert natija.data['brend'] is not None   # ""
        assert natija.data['miqdor'] == 1

    def test_mahsulot_ozgartirish(self):
        mahsulot = {"id": 1,"nom": "nomm1","narx": 1,"miqdor": 1,"brend": "brendd1","kelgan_sana": "2022-11-16","olchov": "olchov1","sotuvchi": 1}
        natija = self.client.put('/mahsulot/6/', data=mahsulot, format='json')
        self.assertEqual(natija.status_code, 202)
        assert natija.data['nom'] == 'nomm1'
        assert natija.data['narx'] == 1


class TestMijozlarView(TestCase):
    def setUp(self) -> None:
        self.client=APIClient()
        token = Token.objects.get(user__username='user1')
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

    def test_hamma_mijozlar(self):
        natija=self.client.get('/mijozlar/')
        assert natija.status_code==200