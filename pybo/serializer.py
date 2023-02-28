from rest_framework import serializers
from .models import Question, Answer

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question # 모델 설정
        fields = ('id','author','subject','content','create_date') # 필드 설정