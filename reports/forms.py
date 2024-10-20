from django import forms


class ClinicForm(forms.Form):
    clinic_name = forms.CharField(max_length=100, label='Clinic Name')
    clinic_logo = forms.ImageField(label='Clinic Logo')
    physician_name = forms.CharField(max_length=100, label='Physician Name')
    physician_contact = forms.CharField(max_length=100, label='Physician Contact')
    patient_first_name = forms.CharField(max_length=100, label='Patient First Name')
    patient_last_name = forms.CharField(max_length=100, label='Patient Last Name')
    patient_contact = forms.CharField(max_length=100, label='Patient Contact')
    patient_dob = forms.DateField(label='Patient DOB', widget=forms.DateInput(attrs={'type': 'date'}))
    chief_complaint = forms.CharField(widget=forms.HiddenInput(), label='Chief Complaint')
    consultation_note = forms.CharField(widget=forms.HiddenInput(), label='Consultation Note')