from rest_framework import serializers

from users.models import User
from reviews.models import Porode, Cats


class UserCastomSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)
        # fields = ('email', 'username')


class PorodeSerializer(serializers.ModelSerializer):
    """Отображения списка пород."""

    class Meta:
        model = Porode
        fields = ('porode_name',)


class CatsListSerializer(serializers.ModelSerializer):
    """Отображения списка котят."""

    class Meta:
        model = Cats
        fields = ('cat_name',)


class CatsSerializer(serializers.ModelSerializer):
    """Создания, обновление котят и отображение котенка."""
    owner = UserCastomSerializer(read_only=True)
    porode_cats = serializers.PrimaryKeyRelatedField(
        queryset=Porode.objects.all()
        )

    class Meta:
        model = Cats
        fields = ('owner', 'porode_cats', 'cat_name', 'color_cat', 'years')

    def create(self, validated_data):
        owner = self.context['request'].user
        porode_cats_data = validated_data.pop('porode_cats')
        porode_cats = Porode.objects.get(id=porode_cats_data.id)
        cats = Cats.objects.create(
            owner=owner,
            porode_cats=porode_cats,
            **validated_data
            )
        return cats
