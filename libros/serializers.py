from django.conf import settings


from rest_framework import serializers


from .models import Libros

# En este se declaran el tipo de fields y si tiene un valor por defecto que se le adjudica en esta funcion misma.
# En este caso en created y updated no son requeridos y se les asigna que el valor sera dado en el momento qque seran creados.
class librosSerializer(serializers.ModelSerializer):
    # Si su <field_name> se declara en su serializador con el parámetro required=False
    # Entonces este paso de validación no tendrá lugar si el campo no está incluido.
    created_at = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)
    updated_at = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)


    class Meta:
        model = Libros
        fields = "__all__"


