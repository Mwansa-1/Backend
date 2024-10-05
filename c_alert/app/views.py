from django.shortcuts import render
from rest_framework import generics, permissions
from .models import ReportForm , Statistics , Alerts , DailyUpdates , Blog , Results
from .serializers import ReportFormSerializer , StatisticsSerializer , AlertsSerializer , DailyUpdatesSerializer , BlogSerializer , ResultsSerializer, UserSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.permissions import IsAuthenticated , IsAdminUser
import cv2
import numpy as np
from django.core.files.uploadedfile import InMemoryUploadedFile
import io



# Create your views here.
# Create Token based Authentication , Update , Delete , List and Create API classes for the serializer classes.

class ReportFormCreateView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = ReportForm.objects.all()
    serializer_class = ReportFormSerializer

class ReportFormCreateView(generics.CreateAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = ReportForm.objects.all()
    serializer_class = ReportFormSerializer

    def perform_create(self, serializer):
        # Get the image from the request
        image = self.request.FILES.get('image')
        
        if image:
            # Process the image
            processed_image, avg_color = self.process_image(image)
            
            # Convert the processed image to an InMemoryUploadedFile
            processed_image_file = self.convert_to_inmemory_file(processed_image, image.name)
            
            # Determine the result based on the average color
            result = self.determine_result(avg_color)
            
            # Save the processed image, average color, and result to the instance
            serializer.save(processed_image=processed_image_file, avg_color=avg_color, result=result)
        else:
            serializer.save()

    def process_image(self, image):
    # Read the image using OpenCV
        image_array = np.asarray(bytearray(image.read()), dtype=np.uint8)
        img = cv2.imdecode(image_array, cv2.IMREAD_COLOR)
        
        # Crop the image (example: crop to the center 100x100 pixels)
        height, width, _ = img.shape
        start_row, start_col = int(height * .25), int(width * .25)
        end_row, end_col = int(height * .75), int(width * .75)
        cropped_img = img[start_row:end_row, start_col:end_col]
        
        # Calculate the average color of the cropped image
        avg_color_per_row = np.average(cropped_img, axis=0)
        avg_color = np.average(avg_color_per_row, axis=0)
        avg_color = avg_color.astype(int)  # Convert to integer values
        
        # Encode the image back to a file-like object
        _, buffer = cv2.imencode('.jpg', cropped_img)
        return buffer.tobytes(), avg_color
    
    def convert_to_inmemory_file(self, image_bytes, original_name):
        # Create a file-like object from the bytes
        image_io = io.BytesIO(image_bytes)
        image_file = InMemoryUploadedFile(
            image_io, None, original_name, 'image/jpeg', image_io.getbuffer().nbytes, None
        )
        return image_file
    
    # Determine the results based on the color range. If it is red, the result is positive, if it is green, the result is negative.
    def determine_result(self, avg_color):
        # Define the color ranges for red and green
        red_lower = np.array([0, 0, 200])
        red_upper = np.array([75, 75, 255])
        green_lower = np.array([0, 200, 0])
        green_upper = np.array([75, 255, 75])
        
        # Check if the average color is within the red range
        if np.all(avg_color >= red_lower) and np.all(avg_color <= red_upper):
            return 'Positive'
        # Check if the average color is within the green range
        elif np.all(avg_color >= green_lower) and np.all(avg_color <= green_upper):
            return 'Negative'
        else:
            return 'Invalid'
        
 
    def results(self, avg_color):
        result = self.determine_result(avg_color)
        return result


    
class ReportFormListView(generics.ListAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = ReportForm.objects.all()
    serializer_class = ReportFormSerializer

class ReportFormUpdateView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = [IsAuthenticated]
    queryset = ReportForm.objects.all()
    serializer_class = ReportFormSerializer


# Create and Update views for the Statistics model
class StatisticsCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class StatisticsListView(generics.ListAPIView):
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

class StatisticsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Statistics.objects.all()
    serializer_class = StatisticsSerializer

# Create and Update views for the Alerts model

class AlertsCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer

class AlertsListView(generics.ListAPIView):
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer

class AlertsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Alerts.objects.all()
    serializer_class = AlertsSerializer

# Create and Update views for the DailyUpdates model

class DailyUpdatesCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = DailyUpdates.objects.all()
    serializer_class = DailyUpdatesSerializer

class DailyUpdatesListView(APIView):
    queryset = DailyUpdates.objects.all()
    serializer_class = DailyUpdatesSerializer

class DailyUpdatesUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = DailyUpdates.objects.all()
    serializer_class = DailyUpdatesSerializer

# Create and Update views for the Blog model

class BlogCreateView(generics.CreateAPIView):
    permission_classes = [IsAdminUser]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogListView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

class BlogUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAdminUser]
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# Create and Update views for the Results model

class ResultsCreateView(generics.CreateAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

class ResultsListView(APIView):
    # permission_classes = [IsAuthenticated]
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

class ResultsUpdateView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [IsAuthenticated]
    queryset = Results.objects.all()
    serializer_class = ResultsSerializer

# User views

class UserRegistrationView(generics.CreateAPIView):
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserLoginView(APIView):
    def post(self, request):
        user = authenticate(username=request.data['username'], password=request.data['password'])
        if user:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=401)





