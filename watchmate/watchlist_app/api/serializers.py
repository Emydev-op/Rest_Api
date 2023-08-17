from rest_framework import serializers
from watchlist_app.models import Movie

class MovieSerializer(serializers.ModelSerializer): # This is a ModelSerializer
    len_name = serializer.SerializerMethodField()
    
    class Meta:
        model = Movie    # This defines the model it will serialize
        fields = "__all__"  #This is used when getting all the fields in the model
        # fields = ['id', 'name', 'description',] #This is used when getting some particular fields in the model
        # exclude = ["_id", "active"] #This is used to remove a particular field from the model

    def get_len_name(self, object):
        return len(object.name)
    
    def validate_name(self, value): #This is used to validate the value in the name field. This is a field validation
        if len(value) < 2:
            raise serializers.ValidationError('Name is too short!')
        else:
            return value
        
    def validate(self, data): #This is used to validate the object. This is an object validation
        if data['name'] == data['description']:
            raise serializers.ValidationError('Name and description should be different')
        else:
            print(data)
            return data

# def name_length(value): #This is a validator function. It is called inside the core argument inside a field
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short!')

# class MovieSerializer(serializers.Serializer): # This is a serializer 
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField(validators=[name_length])
#     description = serializers.CharField()
#     active = serializers.BooleanField()
    
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
    
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
    
#     # def validate_name(self, value):
#     #     if len(value) < 2:
#     #         raise serializers.ValidationError('Name is too short!')
#     #     else:
#     #         return value
        
#     def validate(self, data):
#         if data['name'] == data['description']:
#             raise serializers.ValidationError('Name and description should be different')
#         else:
#             print(data)
#             return data
