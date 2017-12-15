from django.db import models


class Topic(models.Model):
    """사용자가 공부하고 있는 주제입니다."""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환합니다."""
        return self.text


class Entry(models.Model):
    """주제에 관해 공부한 내용(항목)"""
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    # Django 2.0 이 되면서, ForeignKey 필드와 OneToOneField 필드의 on_delete 인자에 대해서도 마이그레이션이 필요합니다.
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        """모델 관리에 필요한 추가 정보를 저장합니다."""
        verbose_name_plural = 'entries'

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환합니다."""
        return self.text[:50] + "..."
