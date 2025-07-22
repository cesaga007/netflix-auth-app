from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('movies.urls')),  # Tu app de películas
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # ← LOGIN
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # ← REFRESH
]
