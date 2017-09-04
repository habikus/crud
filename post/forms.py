from django import forms
from .models import Kisiler
from .models import Kitaplar
from .models import Hareketler
from datetime import datetime
# from bootstrap3_datetime.widgets import DateTimePicker

class KisiForm(forms.ModelForm):
    adsoyad = forms.CharField(label='')
    sinifi = forms.CharField(label='')
    nosu = forms.CharField(label='')
    telefonu = forms.CharField(label='')
    email = forms.CharField(label='')
    aciklama = forms.CharField(label='')

    class Meta:
       model=Kisiler
       fields = [
           'adsoyad',
           'sinifi',
           'nosu',
           'telefonu',
           'email',
           'aciklama',
       ]
class KitapForm(forms.ModelForm):
    class Meta:
       model=Kitaplar
       fields = [
           'kitapadi',
           'yazari',
           'yayinevi',
           'turu',
           'aciklama',
       ]

class HareketForm(forms.ModelForm):
    #alistarihi = forms.DateTimeField(default=datetime.now(), blank=True)
    alistarihi = forms.DateField(label='Alış Tarihi', widget=forms.SelectDateWidget(years=range(2017, 2019)))
    verilistarihi = forms.DateField(label='Veriliş Tarihi', widget=forms.SelectDateWidget(years=range(2017, 2019)))

    class Meta:
         model = Hareketler
         fields = [
             'adsoyad',
             'kitapadi',
             'aciklama',
         ]

class AramaFormu(forms.Form):
    aranacak_kelime = forms.CharField()
    def clean_aranacak_kelime(self):
        kelime = self.cleaned_data['aranacak_kelime']
        if len(kelime) < 3:
            raise forms.ValidationError('Aranacak kelime 3 harften az olamaz !..')
        return kelime
