from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action

from advertisements.filters import AdvertisementFilter
from advertisements.models import Advertisement, Favorites
from advertisements.permissions import IsOwnerOrReadOnly
from advertisements.serializers import AdvertisementSerializer, FavoritesSerializer


class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""
    
    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""

        if self.action in ["create", "update", "partial_update", ]:
            return [IsAuthenticated(), IsOwnerOrReadOnly()]
        return []

    def get_queryset(self):
        """Установка статуса DRAFT."""

        adv_for_all = Advertisement.objects.all().exclude(status="DRAFT")
        if self.request.user.is_superuser is True:
            return Advertisement.objects.all()
        if self.request.user.id is not None and self.request.method in ["GET", "PATCH"]:
            return adv_for_all | Advertisement.objects.filter(status="DRAFT", creator_id=self.request.user.id)
        return adv_for_all

    @action(detail=True, methods=['POST'])
    def add_favourites(self, request, pk):
        """Добавление сообщения в избранное."""

        creator = Advertisement.objects.filter(id=pk).exclude(status="DRAFT")
        result = AdvertisementSerializer(creator, many=True)
        if len(result.data) == 0:
            return Response({'Message': 'Неправильный ID объявления'})
        if result.data[0]['creator']['username'] == str(self.request.user):
            return Response({'Message': 'Вы владелец объявления'})
        if not Favorites.objects.filter(creator=self.request.user, advertisement=pk):
            Favorites.objects.create(creator=self.request.user, advertisement_id=pk)
            return Response({'Message': 'OK'})
        else:
            return Response({'Message': 'Объявление уже добавлено в избранные'})

    @action(detail=False)
    def list_favourites(self, request):
        """Получение списка избранных сообщений пользователя."""

        if request.user.id is None:
            return Response({'Message': 'Авторизуйтесь'})
        queryset = Favorites.objects.filter(creator=self.request.user)
        result = FavoritesSerializer(queryset, many=True)
        return Response(result.data)


class FavoritesViewSet(ModelViewSet):
    queryset = Favorites.objects.all()
    serializer_class = FavoritesSerializer
