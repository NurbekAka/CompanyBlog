from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter
from .views import AdvertisementView, CompanyView, CompanyCreate, CommentListView, CompanyEditView, \
    AdvertisementCreateView, AdEditView, CommentCreateView, CommentEditView, CompanyFavoriteView, \
    CompanyDetail, AdFavoriteView, CompanyFavoriteListView, AdFavoriteListView, AdDetailView, \
    MyAdListView, MyCompanyListView, MyCommentListView, CommentDetailView, CommentFavoriteView, CommentFavoriteListView


router = DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),

    path('signup/', views.signup, name='signup'),

    path('company/list/', CompanyView.as_view()),
    path('company/<int:pk>/', CompanyDetail.as_view()),
    path('company/create/', CompanyCreate.as_view()),
    path('company/edit/<int:pk>/', CompanyEditView.as_view()),
    path('company/favorite/', CompanyFavoriteView.as_view()),
    path('company/favorite/list/', CompanyFavoriteListView.as_view()),
    path('company/my_list/', MyCompanyListView.as_view()),


    path('advertisement/list/', AdvertisementView.as_view()),
    path('advertisement/create/', AdvertisementCreateView.as_view()),
    path('advertisement/<int:pk>/', AdDetailView.as_view()),
    path('advertisement/edit/<int:pk>/', AdEditView.as_view()),
    path('advertisement/favorite/', AdFavoriteView.as_view()),
    path('advertisement/favorite/list/,', AdFavoriteListView.as_view()),
    path('advertisement/my_list/', MyAdListView.as_view()),


    path('comment/list/', CommentListView.as_view()),
    path('comment/create/', CommentCreateView.as_view()),
    path('comment/<int:pk>/', CommentDetailView.as_view()),
    path('comment/edit/<int:pk>/', CommentEditView.as_view()),
    path('comment/my_list/', MyCommentListView.as_view()),
    path('comment/favorite/', CommentFavoriteView.as_view()),
    path('comment/favorite/list/', CommentFavoriteListView.as_view()),



    ]



