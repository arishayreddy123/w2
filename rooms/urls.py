from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import (
    RegisterView, MeView, ConferenceRoomViewSet, ReservationViewSet,
    AdminUserListView, AdminRoomOverview, AdminReservationList,
    AdminDeleteReservation, PromoteUserToAdmin
)

router = DefaultRouter()
router.register(r'rooms', ConferenceRoomViewSet)
router.register(r'reservations', ReservationViewSet)

urlpatterns = [
    # Auth routes
    path('auth/register/', RegisterView.as_view(), name='register'),
    path('auth/me/', MeView.as_view(), name='me'),

    # Admin routes
    path('admin/users/', AdminUserListView.as_view(), name='admin-users'),
    path('admin/rooms/overview/', AdminRoomOverview.as_view(), name='admin-rooms'),
    path('admin/reservations/', AdminReservationList.as_view(), name='admin-reservations'),
    path('admin/reservations/<int:pk>/delete/', AdminDeleteReservation.as_view(), name='admin-delete-reservation'),
    path('admin/users/<int:pk>/promote/', PromoteUserToAdmin.as_view(), name='promote-to-admin'),
]

# Add DRF router URLs (e.g., /rooms/, /reservations/)
urlpatterns += router.urls
