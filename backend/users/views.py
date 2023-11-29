from api.pagination import CustomPageNumberPagination
from api.serializers import (CustomUserSerializer, FollowSerializer,
                             SubscribeSerializer)
from django.shortcuts import get_object_or_404
from djoser.views import UserViewSet
from recipes.models import Subscribe
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import User


class CustomUserViewSet(UserViewSet):
    queryset = User.objects.all()
    serializer_class = CustomUserSerializer
    pagination_class = CustomPageNumberPagination

    @action(detail=True,
            methods=["POST", "DELETE"],
            url_path='subscribe',
            url_name='subscribe',
            permission_classes=[IsAuthenticated])
    def subscribe(self, request, id):
        author = get_object_or_404(User, id=id)
        serializer = FollowSerializer(
            data={'user': request.user.id, 'author': id}
        )
        if request.method == "POST":
            serializer.is_valid(raise_exception=True)
            serializer.save(user=request.user)
            serializer = SubscribeSerializer(author)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        subscribe = get_object_or_404(
            Subscribe,
            user=request.user,
            author__id=id)
        subscribe.delete()
        return Response(f'{request.user} отписался от {subscribe.author}',
                        status=status.HTTP_204_NO_CONTENT)

    @action(
        detail=False,
        permission_classes=[IsAuthenticated]
    )
    def subscriptions(self, request):
        user_obj = User.objects.filter(subscribing__user=request.user)
        paginator = PageNumberPagination()
        paginator.page_size = 6
        result_page = paginator.paginate_queryset(user_obj, request)
        serializer = SubscribeSerializer(
            result_page, many=True, context={'current_user': request.user})
        return paginator.get_paginated_response(serializer.data)
