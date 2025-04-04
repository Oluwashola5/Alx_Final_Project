from django.urls import path, include
from .views import CreateItemView, ItemRetrieveUpdateDestroyView
from .views import CreateItemView, RetrieveItemView, UpdateItemView, DeleteItemView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from rest_framework.authtoken import views
from rest_framework.authtoken.views import obtain_auth_token  # Correct import

urlpatterns = [
    # Other URL patterns
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/', views.obtain_auth_token, name='api-token'),
]

urlpatterns = [
    # path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),
]

urlpatterns = [
    path('items/', CreateItemView.as_view(), name='create-item'),
    path('items/<int:item_id>/', RetrieveItemView.as_view(), name='retrieve-item'),
    path('items/<int:item_id>/update/', UpdateItemView.as_view(), name='update-item'),
    path('items/<int:item_id>/delete/', DeleteItemView.as_view(), name='delete-item'),
]