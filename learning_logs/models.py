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
        verbose_name_plural = 'entries'  # 복수형 이름 직접 지정 (이름을 따로 지정해주지 않으면 장고는 Entrys 라는 복수형을 직접 만들어서 씀 = 틀린 단어)

    def __str__(self):
        """모델에 관한 정보를 문자열 형태로 반환합니다."""
        return self.text[:50] + "..."  # 텍스트의 첫 50자만 표시 + 생략 부호(...)
