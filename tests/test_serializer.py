# from unittest import TestCase
#
# from mainapp.serializers import *
# from mainapp.models import *
#
# class TestMijozSer(TestCase):
#     def setUp(self) -> None:
#         self.data = {
#             "id":5, "ism":"Ali",
#             "nom":"Coca-Cola", "manzil":"Marg'ilon, markaz",
#               "tel":"+998916693704", "qarz":0,
#             "sotuvchi":Sotuvchi.objects.get(id=1)}
#
#     def test_mijoz_ser(self):
#         ser = MijozSerializer(self.data) # Mijoz.objects.all(), many=True
#         assert ser.data['id'] == 5
#         assert ser.data['ism'] == "Ali"
#         assert ser.data['nom'] == "Coca-Cola"
#         assert ser.data['sotuvchi'] == 1
#
#     def test_qarz_valid(self):
#         mijoz = {
#             "id": 5, "ism": "Ali",
#             "nom": "Coca-Cola", "manzil": "Marg'ilon, markaz",
#             "tel": "+998916693704", "qarz": 0,
#             "sotuvchi": 1}
#         ser = MijozSerializer(data=mijoz)
#         assert ser.is_valid() == True
#         assert ser.data['ism'] == 'Ali'
#         assert ser.data['qarz'] == 0
#         assert ser.data['tel'] == "+998916693704"
#
#     def test_qarz_invalid(self):
#         mijoz = {
#             "id": 5, "ism": "Ali",
#             "nom": "Coca-Cola", "manzil": "Marg'ilon, markaz",
#             "tel": "+998916693704", "qarz": 700000,
#             "sotuvchi": 1}
#         ser = MijozSerializer(data=mijoz)
#         assert ser.is_valid() == False
#         assert ser.errors['qarz'][0] == "Mijozda bunday katta qarz bo'lishi mimkin emas!"
