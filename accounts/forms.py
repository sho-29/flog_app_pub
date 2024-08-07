from typing import Any
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django import forms

User = get_user_model()  # こっちで先に変数代入する！


class SignupForm(UserCreationForm):
    class Meta:
        model = User  # model = get_user_model() は NG
        # オブジェクトを作成
        fields = ("username", "email")
    
    def __init__(self, *args: Any, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].help_text = ''
        self.fields["password1"].help_text = ''
        self.fields["password2"].help_text = ''
        self.fields["username"].label_suffix = ''
        self.fields["email"].label_suffix = ''
        self.fields["password1"].label_suffix = ''
        self.fields["password2"].label_suffix = ''

class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']  # 更新したいフィールドを指定

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # フォームの見た目をカスタマイズする場合は、ここで設定します。
        self.fields['username'].label = 'ユーザー名'
        self.fields['email'].label = 'メールアドレス'
        self.fields["username"].help_text = ''
        self.fields['username'].label_suffix = ''
        self.fields['email'].label_suffix = ''
