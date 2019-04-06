from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company, Advertisement, Comment


class CompanyFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('owner', 'company', 'address', 'phone_number', 'info', 'logo', 'id')


class CompanyEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('address', 'logo', 'phone_number', 'info')


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company', 'address', 'logo', 'phone_number', 'info')

    def create(self, validate_data):
        owner = self.context.get('owner')
        company = Company.objects.create(owner=owner, **validate_data)
        company.save()
        return company


class AdFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'advertisement', 'picture', 'company')
        read_only_fields = ('company',)


class AdEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('title', 'advertisement', 'picture')


class AdCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'advertisement', 'picture')


class CommentFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'comment', 'comment_photo', 'company', 'post')

        read_only_fields = ('company', 'post')


class CommentEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('comment', 'comment_photo',)


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('company', 'post', 'comment', 'comment_photo',)
        read_only_fields = ('company', 'post')






class SignUpFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )
