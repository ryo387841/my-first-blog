from django import forms

from .models import User,Division,Content

class NewUserForm(forms.ModelForm):
    class Meta():
        model = User
        #モデルのインスタンス作成

        fields = '__all__'
        #fieldsに__all__をセットすると、モデル内の全てのフィールドが用いられる

class NewDivisionForm(forms.ModelForm):
    class Meta():
        model = Division
        #モデルのインスタンス作成

        fields = '__all__'
        #fieldsに__all__をセットすると、モデル内の全てのフィールドが用いられる

class NewContentForm(forms.ModelForm):
    class Meta():
        model = Content
        #モデルのインスタンス作成

        fields = '__all__'
        #fieldsに__all__をセットすると、モデル内の全てのフィールドが用いられる
