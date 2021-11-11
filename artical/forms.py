from django import forms
def GenForm(Model,listHiddenfield=[]):
    data = {field:forms.HiddenInput() for field in listHiddenfield}
    class newform(forms.ModelForm):
        class Meta:
            model = Model
            exclude = ('id',)
            widgets = data
    return newform
# class OrderNewForm(forms.ModelForm):

#    client = forms.ModelChoiceField(
#        required=False,
#        queryset=Client.objects.all(),
#        widget=RelatedFieldWidgetCanAdd(Client, related_url="so_client_add")
#                                 )
#    class Meta:
#        model = Order
#        fields = ('code', 'client')