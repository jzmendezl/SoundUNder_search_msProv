from rest_framework import viewsets
from rest_framework import filters
from rest_framework.response import Response
from api.models import Song
from api.serializers import SongSerializer

class SongViewSet(viewsets.ModelViewSet):

    serializer_class = SongSerializer
    queryset = Song.objects.all()
    filter_backends = [filters.SearchFilter]
    search_fields = ['author','name','album']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())

        ids = request.query_params.get('ids')
        if ids:
            ids = ids.split(',')
            queryset = queryset.filter(id__in=ids)

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
    
    
    
    