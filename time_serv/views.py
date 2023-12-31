from rest_framework import generics
from .serializers import CurrentTimeSerializer
from rest_framework.response import Response
from datetime import datetime
from rest_framework import status

# Create your views here.
class CurrentTimeApi(generics.RetrieveAPIView):
    serializer_class = CurrentTimeSerializer

    def get_object(self):
        date = datetime.now()
        return {"current_time": date}
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    