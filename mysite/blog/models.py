from django.db import models
from django.utils import timezone
from django.conf import settings


class Company(models.Model):
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    company = models.CharField(max_length=200)
    logo = models.ImageField(upload_to='logo', null=True, blank=True)
    address = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=200)
    info = models.TextField()
    created_date = models.DateTimeField(default=timezone.now())

    class Meta:
        verbose_name = 'Company'
        verbose_name_plural = 'Companies'

    def __str__(self):
        return self.company


class CompanyFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    company = models.ForeignKey(Company, related_name='is_favorite', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite Company'
        verbose_name_plural = 'Favorite Companies'

    def __str__(self):
        return self.company.company


class Advertisement(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    title = models.CharField(max_length=200, null=True, blank=True)
    advertisement = models.TextField()
    picture = models.ImageField(upload_to='picture', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.title


class AdFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    title = models.ForeignKey(Advertisement, related_name='is_favorite', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite Advertisement'
        verbose_name_plural = 'Favorite Advertisements'

    def __str__(self):
        return self.advertisement.title


class Comment(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE, blank=True, null=True)
    post = models.ForeignKey(Advertisement, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.TextField()
    comment_photo = models.ImageField(upload_to='comment-photo', null=True, blank=True)
    created_date = models.DateTimeField(default=timezone.now())

    def __str__(self):
        return self.comment


class CommentFavorite(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, blank=True, null=True)
    comment = models.ForeignKey(Comment, related_name='is_favorite', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Favorite Comment'
        verbose_name_plural = 'Favorite Comments'

    def __str__(self):
        return self.comment.comment

