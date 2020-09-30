from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ..serializers import PublicProfileSerializer
from ..models import Profile

User = get_user_model()

@api_view(['GET', 'POST'])
def profile_detail_api_view(request, username, *args, **kwargs):
    qs= Profile.objects.filter(user__username=username)
    if not qs.exists():
        return Response({"detail": "User not found"}, status=404)
    profile_obj = qs.first()
    data = request.data or {}
    if request.method == 'POST':
        me = request.user
        me.save()
    serializer = PublicProfileSerializer(instance=profile_obj, context={"request": request})        
    return Response(serializer.data, status=200)
