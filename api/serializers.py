from django.contrib.auth.models import AbstractUser
from rest_framework import serializers
from api.models import User,CandidateProfile,Job,CompanyProfile,Application

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=["id","username","email","password","role"]

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)

        
# class CandidateProfileSerializer(serializers.ModelSerializer):
#     id=serializers.CharField(read_only=True)
#     user=UserSerializer(read_only=True)
#     class Meta:
#         model=CandidateProfile
#         fields=["id","user","phone","image","gender","qualification","resume","location","ready_to_relocate","skills","experience"]

# class CompanyProfileSerializer(serializers.ModelSerializer):
#     id=serializers.CharField(read_only=True)
#     user=UserSerializer(read_only=True)
#     class Meta:
#         model=CompanyProfile
#         fields=["id","user","phone","logo","description","location","adress","company_name"]

# class JobSerializer(serializers.ModelSerializer):
#     id=serializers.CharField(read_only=True)
#     company=CompanyProfileSerializer(read_only=True)
#     class Meta:
#         model=Job
#         fields=["id","company","start_date","end_date","title","salary","description","qualification","experience","location","skills"]


# class ApplicationSerializer(serializers.ModelSerializer):
#     id=serializers.CharField(read_only=True)
#     company=CompanyProfileSerializer(read_only=True)
#     job=JobSerializer(read_only=True)
#     candidate=CandidateProfileSerializer(read_only=True)
#     class Meta:
#         model=Application
#         fields=["id","company","job","candidate","options","apply_date"]