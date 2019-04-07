from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AdvertisementView, CompanyView, CompanyCreate, CommentListView, CompanyEditView, \
    AdvertisementCreateView, AdEditView, CommentCreateView, CommentEditView, CompanyFavoriteView, \
    CompanyDetail, AdFavoriteView


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('signup/', views.signup, name='signup'),

    path('company/list/', CompanyView.as_view({'get': 'list'}), name='company_list_api'),
    path('company/<int:pk>/', CompanyDetail.as_view()),
    path('company/create/', CompanyCreate.as_view()),
    path('company/edit/<int:pk>/', CompanyEditView.as_view()),
    path('company/favorite/', CompanyFavoriteView.as_view()),


    path('advertisement/list/', AdvertisementView.as_view({'get': 'list'}), name='advertisement_list_api'),
    path('advertisement/create/', AdvertisementCreateView.as_view()),
    path('advertisement/<int:pk>/', AdvertisementView.as_view({'get':'retrieve', 'delete': 'destroy'}),
         name='advertisement_api'),
    path('advertisement/edit/<int:pk>/', AdEditView.as_view()),
    path('advertisement/favorite/', AdFavoriteView.as_view()),




    path('comment/list/', CommentListView.as_view({'get': 'list'}), name='comment_list_api'),
    path('comment/create/', CommentCreateView.as_view()),
    path('comment/<int:pk>/', CommentListView.as_view({'get':'retrieve', 'delete':'destroy'}),
         name='comment_api'),
    path('comment/edit/<int:pk>/', CommentEditView.as_view()),
    ]



