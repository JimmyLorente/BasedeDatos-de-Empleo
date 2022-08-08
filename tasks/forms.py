import email
from tkinter.tix import Form

from django import forms

class FormularioTrabajo(forms.Form):
    nombres=forms.CharField()
    email=forms.EmailField()
    telefono=forms.NumberInput()
    fecha=forms.DateInput()
    describete=forms.CharField()