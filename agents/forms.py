from django import forms
from leads.models import Agent


class AgentFormModel(forms.ModelForm):
    class Meta:
        model = Agent
        fields = (
            'user',
        )
