from rest_framework import serializers
from .models import Marketplace
from likes.models import Like


class MarketplaceSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source = 'owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source = 'owner.profile.id')
    profile_image = serializers.ReadOnlyField(source = 'owner.profile.image.url')
    like_id = serializers.SerializerMethodField()
    comments_count = serializers.ReadOnlyField()
    likes_count = serializers.ReadOnlyField()

    def validate_image(self, value):
        """checks if image bigger than 2MB, width & height larger than 4096 px"""
        if value.size > 1024 * 1024 * 2:
            raise serializers.ValidationError(
                'Image size larger than 2MB'
            )
        if value.image.width > 4096:
            raise serializers.ValidationError(
                'Image width larger than 4096px'
            )
        if value.image.height > 4096:
            raise serializers.ValidationError(
                'Image height larger than 4096px'
            )
        return value
    
    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    def get_like_id(self, obj):
        user = self.context['request'].user
        if user.is_authenticated:
            like = Like.objects.filter(
                owner=user, marketplace=obj
                ).first()
            # print(like_marketplace)
            return like.id if like else None
        return None
    
    class Meta:
        model = Marketplace
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at', 'updated_at',
            'title', 'content', 'image', 'image_filter',
            'like_id', 'comments_count', 'likes_count',
            'price', 'status', 'condition', 'details',
            'address', 'contact_number', 'email'
        ]


class MarketplaceDetailSerializer(MarketplaceSerializer):
    """Serializer for Marketplace update view. Makes required 
    fields optional for PUT requests."""

    price = models.FloatField(required=False)
    status = models.IntegerField(required=False)
    condition = models.CharField(required=False)
    details = models.TextField(required=False)