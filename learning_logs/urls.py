"""learning_logs의 URL 패턴을 정의합니다."""

from django.conf.urls import url
from . import views

app_name = 'learning_logs'  # Django 2.0 변경사항: namespace 대신 app_name 지정

urlpatterns = [
    # 홈페이지
    url(r'^$', views.index, name='index'),
]
