from rest_framework_simplejwt.serializers import TokenObtainSerializer
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenViewBase


class TokenObtainPairSerializer(TokenObtainSerializer):

    @classmethod
    def get_token(cls, user):
        return RefreshToken.for_user(user)

    def validate(self, attrs):
        data = super().validate(attrs)

        refresh = self.get_token(self.user)

        data['refresh'] = str(refresh)
        data['token'] = str(refresh.access_token)
        data['username'] = str(self.user)
        return data


class Login(TokenViewBase):

    serializer_class = TokenObtainPairSerializer


token_obtain_pair = Login.as_view()



