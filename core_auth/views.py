# from django.shortcuts import render
#
# # Create your views here.
# from djoser.views import UserViewSet as DjoserUserViewSet
#
#
# class UserViewSet(DjoserUserViewSet):
#     def perform_update(self, serializer):
#         # Remove the email sending functionality from the original method
#         instance = serializer.save()
