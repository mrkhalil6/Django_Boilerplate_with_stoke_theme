# from django.db.models import Q
# from apps.authentication.models import Organization
# from apps.authentication.serliazers import GetOrganizationsSerializer
#
#
# def check_super_admin(request):
#     request_user = request.user
#     if request_user and "anonymoususer" not in str(request_user).lower():
#         if request_user.is_super_admin:
#             return {'is_supper_admin_logged_in': True, "selected_organization": request_user.organization.name}
#         else:
#             if request_user.organization:
#                 return {'is_supper_admin_logged_in': False, "selected_organization": request_user.organization.name}
#             else:
#                 return {'is_supper_admin_logged_in': False, "selected_organization": None}
#     return {"is_supper_admin_logged_in": False, "selected_organization": None}
#
#
# def organizations_data(request):
#     admin_check = check_super_admin(request)
#     # print(admin_check)
#     if admin_check.get("is_supper_admin_logged_in"):
#         entity = Organization.objects.filter(~Q(status=4))
#         # print(entity)
#         serialized_entity = GetOrganizationsSerializer(entity, many=True)
#         # return {"organizations_listing_details": serialized_entity.data}
#         return {"organizations_listing_details": serialized_entity.data}
#     else:
#         return {"organizations_listing_details": None}
