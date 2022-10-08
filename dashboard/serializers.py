from .models import Krosovka
from rest_framework import serializers

class LyricsAPI(serializers.ModelSerializer):
    class Meta:
        model = Krosovka
        fields = '__all__'