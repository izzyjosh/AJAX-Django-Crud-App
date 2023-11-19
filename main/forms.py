from django import forms
from .models import PersonInfo


class PersonInfoForm(forms.ModelForm):
    first_name = forms.CharField(
            label="",
            required=True,
            widget = forms.TextInput(attrs={
                "name":"first_name",
                "type":"text",
                "class":"form-control my-2",
                "placeholder":"First Name",
                }))


    last_name = forms.CharField(
            label="",
            required=True,
            widget = forms.TextInput(attrs={
                "name":"last_name",
                "type":"text",
                "class":"form-control my-2",
                "placeholder":"Last Name",
                }))


    department = forms.CharField(
            label="",
            required=True,
            widget = forms.TextInput(attrs={
                "name":"department",
                "type":"text",
                "class":"form-control my-2",
                "placeholder":"Department",
                }))


    course = forms.CharField(
            label="",
            required=True,
            widget = forms.TextInput(attrs={
                "name":"course",
                "type":"text",
                "class":"form-control my-2",
                "placeholder":"course",
                }))

    class Meta:
        model = PersonInfo
        fields = ("__all__")

