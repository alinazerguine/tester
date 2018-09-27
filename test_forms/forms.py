from django import forms

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Field
from crispy_forms.bootstrap import (
    PrependedText, PrependedAppendedText, FormActions)


class KidneyxForm(forms.Form):
    vertexes = forms.IntegerField(label="Vertexes", required=True)
    probability = forms.FloatField(label="Probability", required=True)

    helper = FormHelper()
    helper.form_method = 'POST'
    helper.form_class = 'form-horizontal'
    helper.label_class = 'col-sm-2'
    helper.field_class = 'col-sm-4'
    helper.layout = Layout(
        Field('vertexes', css_class='input-sm'),
        Field('probability', css_class='input-sm'),
        FormActions(Submit('purchase', 'Submit', css_class='btn-primary'))
    )