from django.contrib.auth import get_user_model
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework import exceptions
from rest_framework_simplejwt.exceptions import TokenError

User = get_user_model()

class CookieJWTAuthentication(JWTAuthentication):
    
    """
    Custom authentication class that handles the HTTP Cookie based authentication.
    Authenticate checks the access token in request and validates it.
    If cookie does not exist or validation fails, authentication fails.
    """

    def authenticate(self, request):
        raw_token = request.COOKIES.get("access_token")
        if raw_token is None:
            return None

        try:
            validated_token = self.get_validated_token(raw_token)
        except TokenError as e:
            raise exceptions.AuthenticationFailed(str(e))

        user = self.get_user(validated_token)
        return (user, validated_token)
