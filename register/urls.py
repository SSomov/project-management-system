from django.urls import include, path
from . import views

app_name = 'register'

urlpatterns = [
    path('new-user/', views.register, name='new-user'),
    path('new-company/', views.newCompany, name='new-company'),
    path(
        'users/',
        include([
            path('', views.usersView, name='users'),
            path('profile', views.profile, name='profile'),
            path('<int:profile_id>/', views.user_view, name='user'),
            path('invite/<int:profile_id>/', views.invite, name='invite'),
            path('invites/', views.invites, name='invites'),
            path('invites/accept/<int:invite_id>/',
                 views.acceptInvite,
                 name='accept-invite'),
            path('invites/delete/<int:invite_id>/',
                 views.deleteInvite,
                 name='delete-invite'),
            path('friends/', views.friends, name='friends'),
            path('friends/remove/<int:profile_id>/',
                 views.remove_friend,
                 name='remove-friend'),
        ])),
]
