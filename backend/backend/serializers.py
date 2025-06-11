from rest_framework import serializers
from .models import Survey

class SurveySerializer(serializers.ModelSerializer):
    # Map camelCase frontend fields to snake_case database fields
    ageGroup = serializers.CharField(source='age_group', required=False, allow_blank=True)
    discoverySource = serializers.CharField(source='discovery_source', required=False, allow_blank=True)
    discoveryOther = serializers.CharField(source='discovery_other', required=False, allow_blank=True)
    locationOther = serializers.CharField(source='location_other', required=False, allow_blank=True)
    appUsage = serializers.BooleanField(source='app_usage', required=False)
    appsUsed = serializers.ListField(source='apps_used', required=False)
    appOther = serializers.CharField(source='app_other', required=False, allow_blank=True)
    featurePreferences = serializers.JSONField(source='feature_preferences', required=False)
    barrierOther = serializers.CharField(source='barrier_other', required=False, allow_blank=True)
    
    class Meta:
        model = Survey
        fields = [
            'id', 'ageGroup', 'discoverySource', 'discoveryOther', 
            'location', 'locationOther', 'appUsage', 'appsUsed', 
            'appOther', 'featurePreferences', 'motivation', 
            'willingness', 'barriers', 'barrierOther', 'created_at'
        ]
        
    def create(self, validated_data):
        return Survey.objects.create(**validated_data)
