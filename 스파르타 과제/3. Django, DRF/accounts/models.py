from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    커스텀 사용자 모델
    Django의 기본 User 모델을 확장하여 추가 필드를 포함
    """

    # 프로필 이미지 필드
    # upload_to: 이미지가 저장될 경로 지정
    # null=True, blank=True: 필드를 선택적으로 만듦
    profile_image = models.ImageField(
        upload_to="profile_images/", null=True, blank=True
    )

    # 사용자 자기소개 필드
    # max_length: 최대 500자까지 입력 가능
    # blank=True: 필드를 선택적으로 만듦
    bio = models.TextField(max_length=500, blank=True)

    # 사용자 계정 생성 시간
    # auto_now_add=True: 객체가 처음 생성될 때 자동으로 현재 시간 저장
    created_at = models.DateTimeField(auto_now_add=True)

    # 사용자 정보 최종 수정 시간
    # auto_now=True: 객체가 저장될 때마다 자동으로 현재 시간으로 업데이트
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        """
        사용자 객체를 문자열로 표현할 때 사용
        관리자 페이지 등에서 사용자를 표시할 때 사용됨
        """
        return self.username
