from django import forms


class LinearForm(forms.Form):
    a = forms.IntegerField()
    b = forms.IntegerField()
    x = forms.IntegerField()


class BranchesForm(forms.Form):
    r = forms.IntegerField()
    c = forms.IntegerField()
    b = forms.IntegerField()


class CyclicForm(forms.Form):
    n = forms.IntegerField()
    p = forms.IntegerField()

