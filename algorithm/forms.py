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
    n = forms.IntegerField(max_value=100)
    p = forms.IntegerField(max_value=100000)


class FileForm(forms.Form):
    file = forms.FileField(allow_empty_file=True)
