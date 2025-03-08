from django.contrib import admin
from django.urls import path, include
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny


class Index(APIView):
    permission_classes = [AllowAny]

    def get(self, request):
        return Response({"msg": "hello world"})


urlpatterns = [
    # path("admin/", admin.site.urls),
    path("api/admin/", admin.site.urls),
    # path("api/v1/", include("home.urls")),
    path("api/v1/", include("home.urls")),
    path("api/v2/", Index.as_view()),
]
