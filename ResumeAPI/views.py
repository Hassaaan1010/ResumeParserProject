from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import CandidateSerializer
from .models import Candidate
from .utils.resume_data_extraction import extract_data_from_resume
from .utils.data_sanitization import sanitize_candidate_data
from django_ratelimit.decorators import ratelimit

@ratelimit(key='ip', rate='10/m', method='ALL', burst=True)
@api_view(['POST'])
def extract_resume(request):
    # Check if rate limit is exceeded
    if getattr(request, 'limited', False):
        return Response({'error': 'Rate limit exceeded. Try again later.'}, status=429)

    # Check if resume file is submitted
    if 'resume' not in request.FILES:
        return Response({'Error':'No resume file provided.'}, status=status.HTTP_400_BAD_REQUEST)
    
    resume_file = request.FILES['resume']
    
    try:
        # extract data
        extracted_data = extract_data_from_resume(resume_file)
        
        # sanitize data
        sanitized_data = sanitize_candidate_data(extracted_data)
        
        # Create a new candidate entry
        candidate = Candidate.objects.create(
            first_name=sanitized_data['first_name'],
            email=sanitized_data['email'],
            mobile_number=sanitized_data['mobile_number']
        )
        
        # Serialize and return the response
        serializer = CandidateSerializer(candidate)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        
    except Exception as e:
        print(e)
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)