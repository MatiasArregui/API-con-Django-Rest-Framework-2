from django.shortcuts import render


from rest_framework.response import Response
from rest_framework import viewsets, status


from .serializers import librosSerializer
from .models import Libros, query_libros_by_args


def index(request):
    return render(request, 'index.html')


class librosViewSet(viewsets.ModelViewSet):
    queryset = Libros.objects.all()
    serializer_class = librosSerializer


    def list(self, request, **kwargs):
        try:
            libros = query_libros_by_args(**request.query_params)
            serializer = librosSerializer(libros['items'], many=True)
            result = dict()
            result['data'] = serializer.data
            result['draw'] = libros['draw']
            result['recordsTotal'] = libros['total']
            result['recordsFiltered'] = libros['count']
            return Response(result, status=status.HTTP_200_OK, template_name=None, content_type=None)


        except Exception as e:
            return Response(e, status=status.HTTP_404_NOT_FOUND, template_name=None, content_type=None)


