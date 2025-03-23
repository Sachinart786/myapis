from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import Book
from .serializers import BookSerializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "Book created successfully", "success": True},
                status=status.HTTP_201_CREATED
            )
        return Response(
            {"error": "Invalid data", "details": serializer.errors, "success": False},
            status=status.HTTP_400_BAD_REQUEST
        )

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response({"data": serializer.data, "success": True})

    def retrieve(self, request, *args, **kwargs):
        try:
            book = self.get_object()
            serializer = self.get_serializer(book)
            return Response({"message": "Book found", "data": serializer.data, "success": True})
        except Book.DoesNotExist:
            return Response({"error": "Book not found", "success": False}, status=status.HTTP_404_NOT_FOUND)

    def update(self, request, *args, **kwargs):
        try:
            book = self.get_object()
            serializer = self.get_serializer(book, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(
                    {"message": "Book updated successfully", "data": serializer.data, "success": True}
                )
            return Response({"error": "Update failed", "details": serializer.errors, "success": False}, status=status.HTTP_400_BAD_REQUEST)
        except Book.DoesNotExist:
            return Response({"error": "Book not found", "success": False}, status=status.HTTP_404_NOT_FOUND)

    def destroy(self, request, *args, **kwargs):
        try:
            book = self.get_object()
            book.delete()
            return Response({"message": "Book deleted successfully", "success": True}, status=status.HTTP_204_NO_CONTENT)
        except Book.DoesNotExist:
            return Response({"error": "Book not found", "success": False}, status=status.HTTP_404_NOT_FOUND)


def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }