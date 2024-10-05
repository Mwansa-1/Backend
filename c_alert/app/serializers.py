from rest_framework import serializers
from .models import ReportForm , Statistics , Alerts , DailyUpdates , Blog , Results , CustomUser

# create the serializer classes
class ReportFormSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReportForm
        fields = '__all__'

class StatisticsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Statistics
        fields = '__all__'

class AlertsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Alerts
        fields = '__all__'

class DailyUpdatesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DailyUpdates
        fields = '__all__'

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class ResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Results
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'password')