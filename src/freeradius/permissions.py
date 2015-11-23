from rest_framework import permissions

class IsCurrentUser(permissions.BasePermission):
	"""
	Custom permission to the viewing of an object only if it is our user
	"""

	def has_object_permission(self, request, view, obj):
		if request.user.is_superuser:
			return false

		# Write permissions are only allowed to the owner of the snippet.
		return str(obj.username) == str(request.user)