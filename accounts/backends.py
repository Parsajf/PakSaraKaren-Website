# from django.contrib.auth.backends import BaseBackend
# from django.contrib.auth import get_user_model

# UserModel = get_user_model()

# class EmailBackend(BaseBackend):
#     def authenticate(self, request, username=None, password=None, **kwargs):
#         email = kwargs.get('email') or username
#         try:
#             user = UserModel.objects.get(email=email)
#         except UserModel.DoesNotExist:
#             return None

#         if user.check_password(password):
#             return user
#         return None

#     def get_user(self, user_id):
#         try:
#             return UserModel.objects.get(pk=user_id)
#         except UserModel.DoesNotExist:
            # return None
