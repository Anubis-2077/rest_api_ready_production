from rest_framework import serializers
from notes.models import *



        
class CategorySerializer (serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        
class NoteSerializer(serializers.ModelSerializer):
    # Este campo se usa para la representación (lectura)
    category_details = CategorySerializer(source='categories', many=True, read_only=True)

    # Este campo se usa para la creación y actualización (escritura)
    categories = serializers.PrimaryKeyRelatedField(
        many=True,
        queryset=Category.objects.all(),
        required=False
    )

    class Meta:
        model = Note
        fields = '__all__'
        extra_kwargs = {
            'categories': {'write_only': True}
        }