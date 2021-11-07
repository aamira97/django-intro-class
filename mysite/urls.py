from django.contrib import admin
from django.urls import path, include
from users import views as user_views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
from django.views.generic import TemplateView
from post.views import AboutView, PostView, PostDetailView, PostCreateView, \
    PostUpdateView, PostDeleteView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('myfirstapp.urls')),
    path('human/', include('homework2.urls')),
    path('register/', user_views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('profile/', user_views.profile, name='profile'),
    path('contact_us/', user_views.contact, name='contact_us'),
    path('success/', user_views.thank_you, name='thank_you'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='users/password_reset.html'), name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='users/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='users/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='users/password_reset_complete.html'),
         name='password_reset_complete'),
    # path('about/', TemplateView.as_view(template_name="about.html")),
    path('about/', AboutView.as_view()),
    path('', PostView.as_view(), name='posts-home'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/update/<int:pk>', PostUpdateView.as_view(), name='post-update'),
    path('post/delete/<int:id>', PostDeleteView.as_view(), name='post-delete')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
