from django.contrib.auth.models import User
from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from advertisements.models import Advertisement, Favorites


class UserSerializer(serializers.ModelSerializer):
    """Serializer для пользователя."""

    class Meta:
        model = User
        fields = ('id', 'username', 'first_name',
                  'last_name', 'is_superuser')


class AdvertisementSerializer(serializers.ModelSerializer):
    """Serializer для объявления."""

    creator = UserSerializer(
        read_only=True,
    )

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'description', 'creator',
                  'status', 'created_at', )

    def create(self, validated_data):
        """Метод для создания"""

        # Простановка значения поля создатель по-умолчанию.
        # Текущий пользователь является создателем объявления
        # изменить или переопределить его через API нельзя.
        # обратите внимание на `context` – он выставляется автоматически
        # через методы ViewSet.
        # само поле при этом объявляется как `read_only=True`
        validated_data["creator"] = self.context["request"].user
        return super().create(validated_data)

    def validate(self, data):
        """Метод для валидации. Вызывается при создании и обновлении."""
        quantity_open_adv = Advertisement.objects.filter(creator=self.context['request'].user.id, status='OPEN')
        result = UserSerializer(quantity_open_adv, many=True)
        if 'status' in data:
            if len(result.instance) >= 10 and data['status'] == 'OPEN':
                raise ValidationError('Количество открытых сообщений больше 10')
        else:
            if len(result.instance) >= 10:
                raise ValidationError('Количество открытых сообщений больше 10')

        return data


class FavoritesSerializer(serializers.ModelSerializer):
    """Serializer для избранных объявлений."""

    advertisement = AdvertisementSerializer(read_only=True, )

    class Meta:
        model = Favorites
        fields = ('id', 'advertisement', )
