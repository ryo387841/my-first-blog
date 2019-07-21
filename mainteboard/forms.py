from django import forms

from .models import Regist
import bootstrap_datepicker_plus as datetimepicker
'''
class NewRegistForm(forms.ModelForm):
    class Meta():
        model = Regist
        #モデルのインスタンス作成

        fields = '__all__'
        #fieldsに__all__をセットすると、モデル内の全てのフィールドが用いられる
'''
class NewRegistForm(forms.ModelForm):
    class Meta:
        model = Regist
        fields = ('shikakebi', 'kiboubi', 'hinban', 'kataban', 'kubun', 'naiyo', 'mitsumorikosu', 'minaoshikosu', 'user')
        widgets = {
            'shikakebi': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),

            'kiboubi': datetimepicker.DatePickerInput(
                format='%Y-%m-%d',
                options={
                    'locale': 'ja',
                    'dayViewHeaderFormat': 'YYYY年 MMMM',
                }
            ),
        }
