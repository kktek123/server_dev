from rest_framework.views import APIView
from rest_framework.response import Response
from .models import LoginUser


class RegistUser(APIView):
    def post(self, request):
        user_id = request.data.get('user_id', "")
        user_pw = request.data.get('user_pw', "")

        if LoginUser.objects.filter(user_id=user_id).exists():
            data = dict(
                msg="The ID that already exists."
            )
            return Response(data)

        LoginUser.objects.create(user_id=user_id, user_pw=user_pw)

        data = dict(
            user_id=user_id,
            user_pw=user_pw
        )

        return Response(data=data)