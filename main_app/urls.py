from django.urls import path
from . import views


urlpatterns = [
    
path('', views.home, name='home'),
path('about/', views.about, name='about'),
path('liveables/', views.liveables_index, name='index'),
path('liveables/<int:liveable_id>', views.liveables_detail, name='liveables_detail'),
path('liveables/create/', views.LiveableCreate.as_view(), name='liveables_create'),
path('liveables/<int:pk>/update/', views.LiveableUpdate.as_view(), name='liveables_update'),
path('liveables/<int:pk>/delete/', views.LiveableDelete.as_view(), name='liveables_delete'),
path('liveables/<int:liveable_id>/assoc_listing/<int:listing_id>', views.assoc_listing, name='assoc_listing'),
path('listings/', views.ListingList.as_view(), name='listings_index'),
path('listings/<int:pk>/', views.ListingDetail.as_view(), name='listings_detail'),
path('listings/<int:pk>/update', views.ListingUpdate.as_view(), name='listings_update'),
path('listings/<int:pk>/delete', views.ListingDelete.as_view(), name='listings_delete'),
path('accounts/signup/', views.signup, name='signup'),

]
