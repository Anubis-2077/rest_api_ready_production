from rest_framework import viewsets
from .serializer import *
from .models import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status


class NoteView(viewsets.ModelViewSet):
    serializer_class = NoteSerializer
    queryset = Note.objects.all()

    def perform_create(self, serializer):
        try:
            serializer.save()
        except Exception as e:
            print("Datos recibidos:", serializer.validated_data)
            print("Error:", e)
            
    @action(detail=True, methods=['post'])
    def toggle_archive(self, request, pk=None):
        note = self.get_object()
        note.is_archived = not note.is_archived
        note.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer