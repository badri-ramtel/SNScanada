from django import forms

class FeedBackForm(forms.Form):
    fname = forms.CharField(max_length= 100, required= True)
    email = forms.EmailField()
    address = forms.CharField(max_length= 200, required= True)
    contact = forms.IntegerField(min_value= 10, max_value= 10)
    feedback = forms.Textarea()
