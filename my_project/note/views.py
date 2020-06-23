from .models import NoteModel
from rest_framework import generics
from .serializers import NoteSerializer

class NoteListView(generics.ListCreateAPIView):
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer

class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    # permission_classes = (IsAuthorOrReadOnly,)
    queryset = NoteModel.objects.all()
    serializer_class = NoteSerializer
