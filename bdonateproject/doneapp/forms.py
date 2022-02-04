from django import forms
from.models import Booking,City

class BookForm(forms.ModelForm):
    class Meta:
        model=Booking
        fields = 'name', 'age', 'address', 'district', 'city', 'bgroup', 'mob'
    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['city'].queryset=City.objects.none()

        if 'district' in self.data:
            try:
                district_id=int(self.data.get('district'))
                self.fields['city'].queryset=City.objects.filter(district_id=district_id).order_by('name')
            except(ValueError,TypeError):
                pass
        elif self.instance.pk:
            self.fields['city'].queryset=self.instance.district.city_set.order_by('name')


