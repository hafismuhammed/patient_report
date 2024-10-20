import base64
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from django.utils import timezone
from django.template.loader import get_template
from xhtml2pdf import pisa
from .forms import ClinicForm
from reports.utils import get_ip_address


class ClinicReportView(View):
    template_name = 'clinic_form.html'

    def get(self, request):
        form = ClinicForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = ClinicForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            context = form.cleaned_data

            if 'clinic_logo' in request.FILES:
                logo = request.FILES['clinic_logo'].read()
                context['clinic_logo'] = base64.b64encode(logo).decode('utf-8')

            context['timestamp'] = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
            context['ip_address'] = get_ip_address(request)

            template = get_template('report.html')
            html = template.render(context)

            response = HttpResponse(content_type='application/pdf')
            file_name = f"CR_{context['patient_last_name']}_{context['patient_first_name']}_{context['patient_dob']}.pdf"
            response['Content-Disposition'] = f'attachment; filename="{file_name}"'

            pdf_status = pisa.CreatePDF(html, dest=response, link_callback=None)

            if pdf_status.err:
                return HttpResponse('Error generating PDF', status=400)

            return response
        else:
            return render(request, self.template_name, {'form': form})
