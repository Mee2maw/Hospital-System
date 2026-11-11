class PatientForm(forms.ModelForm):
    class Meta:
        model = patient
        fields = '__all__'

    widgets = {
        'patient_id': forms.TextInput( attrs={'class': 'form-control'}),
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'age': forms.NumberInput(attrs={'class': 'form-control'}),
        'gender': forms.Select(attrs={'class': 'form-control'}),
        'address': forms.Textarea(attrs={'class': 'form-control'}),
        'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        'medical_history': forms.Textarea(attrs={'class': 'form-control'}),
    }