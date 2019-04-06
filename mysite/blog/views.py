from django.shortcuts import render
from .models import Company, Comment, Advertisement
from django.shortcuts import redirect
from django.contrib.auth import login, authenticate
from .forms import SignUpForm
from .serializers import CompanyFormSerializer, AdFormSerializer, CommentFormSerializer, \
    CompanyCreateSerializer, AdCreateSerializer, CommentCreateSerializer, \
    CompanyEditSerializer, AdEditSerializer, CommentEditSerializer
from rest_framework import viewsets, generics, status
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .permission import IsCompanyOwner, IsAdsCompanyOwner, IsCommentsCompanyOwner
from rest_framework.response import Response
from .pagination import ListPagination


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('blog/signup.html')
    else:
        form = SignUpForm()
        return render(request, 'blog/signup.html', {'form': form})


def mainUrl(request):
    return render(request, 'blog/main.html', {})


class CompanyView(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanyFormSerializer
    lookup_field = 'pk'
    pagination_class = ListPagination


class CompanyCreate(generics.CreateAPIView):
    serializer_class = CompanyCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def get_serializer_context(self):
        context = super(CompanyCreate, self).get_serializer_context()
        context.update({
            'owner': self.request.user
        })
        return context


class CompanyEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Company.objects.all()
    serializer_class = CompanyEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsCompanyOwner)


class AdvertisementView(viewsets.ModelViewSet):
    queryset = Advertisement.objects.all()
    serializer_class = AdFormSerializer
    lookup_field = 'pk'
    pagination_class = ListPagination


class AdvertisementCreateView(generics.CreateAPIView):
    serializer_class = AdCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Company.objects.get(pk=request.data['company'])
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Advertisement created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'You do not have any permission to create advertisement here!!!'},
                            status=status.HTTP_400_BAD_REQUEST)


class AdEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Advertisement.objects.all()
    serializer_class = AdEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsAdsCompanyOwner)


class CommentListView(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentFormSerializer
    lookup_field = 'pk'
    pagination_class = ListPagination


class CommentCreateView(generics.CreateAPIView):
    serializer_class = CommentCreateSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        company = Company.objects.get(pk=request.data['company'])
        if company.owner == self.request.user:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response({'Comment created successfully'}, status=status.HTTP_201_CREATED, headers=headers)
        else:
            return Response({'You do not have permissions to create comment here!!!'},
                            status=status.HTTP_400_BAD_REQUEST)


class CommentEditView(generics.UpdateAPIView):
    lookup_field = 'pk'
    queryset = Comment.objects.all()
    serializer_class = CommentEditSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAuthenticated, IsCommentsCompanyOwner)

