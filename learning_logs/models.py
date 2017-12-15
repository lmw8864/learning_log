from django.db import models


class Topic(models.Model):
    """사용자가 공부하고 있는 주제입니다."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환합니다."""
        return self.text
