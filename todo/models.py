from django.db import models

PRIORITY = {
    ('0', '보통'),
    ('1', '중요'),
    ('2', '매우중요')
}


class Todo(models.Model):
    title = models.CharField(max_length=100)
    priority = models.CharField(max_length=1, choices=PRIORITY, default=0)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    deadline = models.DateTimeField(null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def summary(self):
        if len(self.content)>200:
            return self.content[:200] + '...'
        return self.content


'''
* 새로운 투두 (제목/내용) 작성
* 목록
* 항목의 제목/내용 수정 가능
* 삭제 가능
* 마감기한
* 우선순위 조절
* 완료처리
* 마감지난거 알람 노출
'''