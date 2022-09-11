from rest_framework.serializers import (ModelSerializer, DateField, ValidationError,
                                        SerializerMethodField, ImageField, CharField, EmailField, IntegerField,
                                        DateTimeField)
from .models import Organization, User
from common.enum import get_user_type, get_user_status, get_status


class GetOrganizationsSerializer(ModelSerializer):
    users_count = SerializerMethodField('get_user_count', required=False)
    status = SerializerMethodField('get_status', required=False)

    def get_user_count(self, obj):
        users_count = User.objects.filter(organization_id=obj.org_id).count()
        return users_count

    def get_status(self, obj):
        return get_status(status=obj.status)

    class Meta:
        model = Organization
        fields = "__all__"


class GetUserSerializer(ModelSerializer):
    user_image = SerializerMethodField('get_user_image', required=False)
    type = SerializerMethodField('get_type', required=False)
    status = SerializerMethodField('get_status', required=False)
    user_full_name = SerializerMethodField('get_user_full_name', required=False)
    user_organization_name = SerializerMethodField('get_user_organization_name', required=False)

    def get_user_image(self, obj):
        try:
            photo_url = obj.user_image.url
            # print("PHOTO URL: ", photo_url)
            return self.context['request'].build_absolute_uri(photo_url)
        except Exception as e:
            # print(e)
            return None

    def get_type(self, obj):
        return get_user_type(obj.type)

    def get_status(self, obj):
        return get_status(status=obj.status)

    def get_user_full_name(self, obj):
        return obj.get_full_name()

    def get_user_organization_name(self, obj):
        return obj.organization.name

    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'username', 'date_of_birth', 'user_image', 'type',
                  'created_by_id', "is_organization_admin", "is_super_admin", "user_full_name",
                  'user_organization_name', 'status', 'date_joined']
