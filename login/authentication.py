from django.contrib.auth.models import User

class AutoCreateUserBackend:
    def authenticate(self, request, username=None, password=None):
        # Check if user already exists
        user = User.objects.filter(username=username).first()
        
        if user:
            return user  # Return existing user
        
        # If user does not exist, create a new one
        user = User.objects.create_user(username=username, password=password)
        return user

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
