from .models import Lyrics
from rest_framework import serializers

class LyricsAPI(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = '__all__'