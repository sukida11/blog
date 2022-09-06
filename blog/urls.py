from django.urls import path

from .views import *

app_name = 'blog'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('registration/', RegistrationUserView.as_view(), name='registration'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('logout/', logout_func, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('create-profile/', CreateProfileInfoView.as_view(), name='create_profile'),
    path('change-profile-info/', ChangeProfileInfoView.as_view(), name='change_profile'),
    path('create-chanel/', CreateChanelView.as_view(), name='create_chanel'),
    path('my-channels/', MyChanel.as_view(), name='my_chanel'),
    path('admin-channels/<int:pk>/', ChannelView.as_view(), name='admin_channels'),
    path('delete-chanel/<int:pk>/', delete_chanel, name='delete_chanel'),
    path('all-channels/', AllChannelsView.as_view(), name='all_channels'),
    path('check-channel/<int:pk>/', ChannelView.as_view(), name='view_channel'),
    path('create-post/', CreatePostView.as_view(), name='create_post'),
    path('post-list/', AllPostView.as_view(), name='post-list'),
    path('check-post/<int:pk>/', PostView.as_view(), name='check_post'),
    path('change-post/<int:pk>/', ChangePostView.as_view(), name='change_post'),
    path('add-admin-to/<int:pk>/', AddAdminView.as_view(), name='add_admin'),
    path('find-user/', FindUserView.as_view(), name='find_user')
]

