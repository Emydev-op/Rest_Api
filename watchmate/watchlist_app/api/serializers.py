from rest_framework import serializers
from watchlist_app.models import WatchList, StreamPlatform, Review

class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)
    class Meta:
        model = Review
        exclude = ('watchlist',)
        # fields = '__all__'

class WatchListSerializer(serializers.ModelSerializer): # This is a ModelSerializer
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList    # This defines the model it will serialize
        fields = "__all__"  #This is used when getting all the fields in the model
        # fields = ['id', 'name', 'description',] #This is used when getting some particular fields in the model
        # exclude = ["_id", "active"] #This is used to remove a particular field from the model

class StreamPlatformSerializer(serializers.ModelSerializer):
    #watchlist = WatchListSerializer(many=True, read_only=True) #This is used when getting all the fields in the watchlist
    watchlist = serializers.StringRelatedField(many=True, read_only=True) #This is used when getting the name of the fields identified by the __str__ in the watchlist
    class Meta:
        model = StreamPlatform
        fields = "__all__"


# def name_length(value): #This is a validator function. It is called inside the core argument inside a field
#     if len(value) < 2:
#         raise serializers.ValidationError('Name is too short!')

# class WatchListSerializer(serializers.Serializer): # This is a serializer 
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
