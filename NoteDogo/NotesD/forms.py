from django import forms

class NewNote(forms.Form):
    Titulo=forms.CharField(max_length=30,widget=forms.TextInput(attrs={'class' : 'card-title', 'value':'Nota nueva'}))
    Nota=forms.CharField(widget=forms.Textarea(attrs={'class':'text-ar materialize-textarea','autofocus':'true','id':'"textarea1"'}))
    
