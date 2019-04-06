from rest_framework.permissions import BasePermission
from .models import Company, Advertisement, Comment


class IsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        company = Company.objects.get(pk=view.kwargs['pk'])
        if company.owner == request.user:
            return True


class IsAdsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        advertisement = Advertisement.objects.get(pk=view.kwargs['pk'])
        if advertisement.company.owner == request.user:
            return True


class IsCommentsCompanyOwner(BasePermission):
    def has_permission(self, request, view):
        if 'pk' not in view.kwargs:
            return False
        comment = Comment.objects.get(pk=view.kwargs['pk'])
        if comment.company.owner == request.user:
            return True
