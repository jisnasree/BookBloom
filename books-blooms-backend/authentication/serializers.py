from .models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'password','first_name','last_name','terms_accepted_at',
            'email_verified_at',]
        extra_kwargs = {
            'password': {'write_only': True},
            'email': {'required': True},
        }

    def validate_email(self, value):
        value = value.strip().lower()
        if User.objects.filter(email__iexact=value).exists():
            raise serializers.ValidationError('A user with this email already exists.')
        return value

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(username=validated_data['email'], **validated_data)
        user.set_password(password)
        user.save()
        return user


















# class UserSerializer(serializers.ModelSerializer):
#     # email = serializers.EmailField(max_length=150)

#     class Meta:
#         model = User
#         fields = ['id', 'username', 'email', 'password']

#         extra_kwargs = {
#         'password': {'write_only': True},
#         }
        
#     def validate_email(self, value):
#         if User.objects.filter(email__iexact=value).exists():
#             raise serializers.ValidationError(
#                 'A user with this email already exists.'
#             )
#         return value.lower().strip()
    
#     def create(self, validated_data):
#         password = validated_data.pop('password')

#         # user = User(
#         # username=validated_data['email'],
#         # **validated_data
#         # )
        
#         user.set_password(password)
#         user.save()

#         return user     
        
#     # def validate_email(self, value):
#     #     value = value.strip().lower()
#     #     if User.objects.filter(username__iexact=value).exists():
#     #         raise serializers.ValidationError('A user with this email already exists.')
#     #     return value

#     # def create(self, validated_data):
#     #     email = validated_data['email']
#     #     user = User(username=email, email=email)
#     #     user.set_unusable_password()
#     #     user.save()
#     #     return user
