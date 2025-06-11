from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import SurveySerializer

@api_view(['POST'])
def SurveySubmitAPI(request):
    import json
    print("Raw request body:", request.body)
    print("Parsed request data:", json.dumps(request.data, indent=2))

    # Use the serializer to handle the camelCase to snake_case mapping
    serializer = SurveySerializer(data=request.data)
    
    if serializer.is_valid():
        survey = serializer.save()
        print("✅ Saved data:", SurveySerializer(survey).data)
        return Response({'message': 'Survey submitted successfully'}, status=status.HTTP_201_CREATED)
    
    print("❌ Validation error:", serializer.errors)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
