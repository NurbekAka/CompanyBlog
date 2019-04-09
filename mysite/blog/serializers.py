from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Company, Advertisement, Comment, CompanyFavorite, AdFavorite, CommentFavorite


class CompanyFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyFavorite
        fields = ('company',)

    def create(self, validated_data):
        user = self.context.get('user')
        fav_company = CompanyFavorite.objects.create(user=user, **validated_data)
        fav_company.save()
        return fav_company


class AdFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'advertisement', 'picture', 'company')
        read_only_fields = ('company',)


class CompanyFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = Company
        fields = ('owner', 'company', 'address', 'phone_number', 'info', 'logo', 'id')


class CompanyDetailSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()
    post_company = AdFormSerializer

    class Meta:
        model = Company
        fields = ('company', 'address', 'logo', 'info', 'owner', 'id', 'is_favorite', 'post_company')

    def get_is_favorite(self, obj):
        user = self.context.get('user')
        favorite = CompanyFavorite.objects.filter(user=user, company=obj)
        if favorite:
            return True
        else:
            return False


class CompanyEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('address', 'logo', 'phone_number', 'info')


class CompanyCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ('company', 'address', 'logo', 'phone_number', 'info', 'id')

    def create(self, validated_data):
        owner = self.context.get('owner')
        company = Company.objects.create(owner=owner, **validated_data)
        company.save()
        return company


class AdFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdFavorite
        fields = ('title',)

        def create(self, validated_data):
            user = self.context.get('user')
            fav_advertisement = AdFavorite.objects.filter(user=user, **validated_data)
            fav_advertisement.save()
            return fav_advertisement


class AdDetailSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Advertisement
        fields = ('company', 'title', 'advertisement', 'id', 'is_favorite')

    def get_is_favorite(self, obj):
        user = self.context.get('user')
        favorite = AdFavorite.objects.filter(user=user, title=obj)
        if favorite:
            return True
        else:
            return False


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


class CommentFavoriteSerializer(serializers.ModelSerializer):
    class Meta:
        model = CommentFavorite
        fields = ('comment',)

        def create(self, validated_data):
            user = self.context.get('user')
            fav_comment = AdFavorite.objects.filter(user=user, **validated_data)
            fav_comment.save()
            return fav_comment


class CommentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('company', 'post', 'comment', 'comment_photo')


class CommentDetailSerializer(serializers.ModelSerializer):
    is_favorite = serializers.SerializerMethodField()

    class Meta:
        model = Comment
        fields = ('company', 'post', 'comment', 'id', 'is_favorite')

    def get_is_favorite(self, obj):
        user = self.context.get('user')
        favorite = CommentFavorite.objects.filter(user=user, comment=obj)
        if favorite:
            return True
        else:
            return False




class SignUpFormSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2', )


