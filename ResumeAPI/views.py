from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CandidateSerializer
from .models import Candidate
from .utils.resume_data_extraction import extract_data_from_resume
# from .utils import extract_data_from_resume, sanitize_data


@api_view(['POST'])
def extract_resume(request):
    if 'resume' not in request.FILES:
        return Response({'Error':'No resume file provided.'}, status=status.HTTP_400_BAD_REQUEST)
    
    resume_file = request.FILES['resume']
    
    try:
        # extract data
        extracted_data = extract_data_from_resume(resume_file)
        
        # Create a new candidate entry
        candidate = Candidate.objects.create(
            first_name=extracted_data['first_name'],
            email=extracted_data['email'],
            mobile_number=extracted_data['mobile_number']
        )
        
        # Serialize and return the response
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)