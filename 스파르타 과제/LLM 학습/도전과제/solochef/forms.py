from django import forms


class ChatForm(forms.Form):
    message = forms.CharField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "오늘 메뉴 추천!"}
        ),
        label="메시지",
    )
