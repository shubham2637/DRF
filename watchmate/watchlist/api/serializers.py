from rest_framework import serializers

from watchlist.models import WatchList, StreamPlatform, Review


# def description_length(value):  # custom validators
#     if len(value) < 5:
#         raise serializers.ValidationError( "Description is too short!" )
#     return value
#
#
# class MovieSerializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only=True)
#     name = serializers.CharField()
#     description = serializers.CharField(validators=[description_length])
#     active = serializers.BooleanField()
#
#     def create(self, validated_data):
#         return Movie.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.description = validated_data.get('description', instance.description)
#         instance.active = validated_data.get('active', instance.active)
#         instance.save()
#         return instance
#
#     def validate_name(self, value):  # field level validation
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         return value
#
#     def validate(self, data):  # Object level validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different")
#         return data
# class MovieSerializer(serializers.ModelSerializer):
#     length_name = serializers.SerializerMethodField()  # custom serializer fields
#
#     class Meta:
#         model = WatchList
#         fields = "__all__"  # all fields
#         fields = ['id', 'name', 'description']
#         exclude = ['active']
#
#     def get_length_name(self, instance):
#         return len(instance.name)
#
#     def validate_name(self, value):  # field level validation
#         if len(value) < 2:
#             raise serializers.ValidationError("Name is too short!")
#         return value
#
#     def validate(self, data):  # Object level validation
#         if data['name'] == data['description']:
#             raise serializers.ValidationError("Name and Description should be different")
#         return data


class ReviewSerializer(serializers.ModelSerializer):
    review_user = serializers.StringRelatedField(read_only=True)

    class Meta:
        model = Review
        exclude = ['watchlist']
        # fields = "__all__"


class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)

    class Meta:
        model = WatchList
        fields = "__all__"  # all fields


class StreamPlatformSerializer(serializers.HyperlinkedModelSerializer):
    # watchlist = WatchListSerializer(many=True, read_only=True)  # related name is watchlist
    # watchlist = serializers.StringRelatedField(many=True)  # related name is watchlist
    watchlist = serializers.HyperlinkedRelatedField(
        many=True,
        read_only=True,
        view_name='movie-details'  # url name for movie
    )

    class Meta:
        model = StreamPlatform
        fields = "__all__"  # all fields
