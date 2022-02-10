from django import forms
from .models import User
from argon2 import PasswordHasher, exceptions

class MypageForm(forms.ModelForm):
    user_image = forms.ImageField(
        label='프로필 사진',
        required=True,
        widget=forms.FileInput(
            attrs={
                'class' : 'user-imgae',
                'placeholder' : '프로필 사진'
            }
        ),
        error_messages={
        'unique' : '이미지를 선택해주세요.'}
    )
    
    class Meta:
        model = User
        fields = [
            'user_image',
        ]
        