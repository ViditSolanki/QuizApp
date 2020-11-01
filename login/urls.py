from django.urls import path
from . import views
from . import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.splash, name='splash'),
    path('login',views.login,name="login"),
    path('password-change/done', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
    path('password-change', auth_views.PasswordChangeView.as_view(template_name='password_change.html'), name='password_change'),
    path('password-reset', auth_views.PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path('password-reset/done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>', auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),
    path('question',views.question,name="question"),
    path('question1',views.question1,name="question1"),
    path('question2',views.question2,name="question2"),
    path('question3',views.question3,name="question3"),
    path('topic',views.topic,name="topic"),
    path('end',views.end,name="end")
]