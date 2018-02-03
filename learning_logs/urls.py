"""learning_logs의 URL 패턴을 정의합니다."""

from django.conf.urls import url
from . import views

app_name = 'learning_logs'

urlpatterns = [
    # 홈페이지
    url(r'^$', views.index, name='index'),
]
