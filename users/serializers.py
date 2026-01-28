from rest_framework import serializers

from users.models import Users

class UsersSerializers(serializers.Serializer):

    id = serializers.IntegerField(read_only=True)

    first_name = serializers.CharField()

    last_name = serializers.CharField()

    user_name = serializers.CharField()

    email = serializers.EmailField()

    age = serializers.IntegerField()

    bio = serializers.CharField()

    password = serializers.CharField()

    created_at = serializers.DateTimeField(read_only=True)


    def validate(self, data):


        first_name = data.get("first_name")
        last_name = data.get("last_name")
        if not (first_name.isalpha()) or not (last_name.isalpha()):
            raise serializers.ValidationError("Enter alphabets only")
        
        user_name = data.get("user_name")
        qs_user_name = Users.objects.filter(user_name=user_name)
        if qs_user_name.exists():
            raise serializers.ValidationError("Username not available")

        email = data.get("email")
        qs_email = Users.objects.filter(email=email)
        if qs_email.exists():
            raise serializers.ValidationError("Email already exists")
        
        age = data.get("age")
        if age is not None and (age < 1 or age > 100):
            raise serializers.ValidationError("Enter age between 1 and 100")
        
        if len(data.get("password")) < 8:
            raise serializers.ValidationError("Password contains atleast 8 characters")
        if data.get("password").isalpha() or data.get("password").isdigit():
            raise serializers.ValidationError("Enter strong password with combination of alphanumeric characters") 

        return data
    





