from django.urls import path
from pybo.views import MovieViewSet
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include, re_path
app_name = 'pybo'

urlpatterns = [
    #path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    #path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('change-password/',auth_views.PasswordChangeView.as_view()),    
    path('answer/vote/<int:answer_id>/', views.answer_vote, name='answer_vote'),
    path('question/vote/<int:question_id>/', views.question_vote, name='question_vote'),
    path('answer/delete/<int:answer_id>/', views.answer_delete, name='answer_delete'),
    path('answer/modify/<int:answer_id>/', views.answer_modify, name='answer_modify'),
    path('question/delete/<int:question_id>/', views.question_delete, name='question_delete'),
    path('question/modify/<int:question_id>/', views.question_modify, name='question_modify'),
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),
    #path('question/create/', views.question_create, name='question_create'),
    path('profile/base/', views.user_profile, name='user_profile'),
    path('profile/question/', views.user_question, name='user_question'),
    path('profile/answer/', views.user_answer, name='user_answer'),
    path('profile/comment/', views.user_comment, name='user_comment'),
    path('password_reset/', views.UserPasswordResetView.as_view(), name="password_reset"),
    path('password_reset/done/', views.UserPasswordResetDoneView.as_view(), name="password_reset_done"),
    path('alexander/', views.index2, name='index2'),
    path('question/craete/<str:category_name>/', views.question_create, name='question_create'),
    path('question/list/', views.index, name='index'),
    path('question/list/<str:category_name>/', views.index, name='index'),
    path('question/detail/<int:question_id>/', views.detail, name='detail'),
    path('expert/', views.expert, name='expert'),
    path('expert/craete/<str:category_name>/', views.expert_create, name='expert_create'),
]

