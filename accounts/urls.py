from django.urls import path
from allauth.account.views import LoginView, LogoutView
from .views import SignupPageView, UserPageView, ProfileView, UpdateProfileView

urlpatterns = [
    path('login/', LoginView.as_view(), name="account_login"),
    path('logout/', LogoutView.as_view(), name="account_logout"),
    path('signup/', SignupPageView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name="profile"),
    path('profile/edit/', UpdateProfileView.as_view(), name="editprofile"),
    path('<str:username>/', UserPageView.as_view(), name="userpage"),

]