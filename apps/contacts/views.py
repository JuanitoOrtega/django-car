from django.shortcuts import redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from django.template.loader import render_to_string


# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        car_price = request.POST['car_price']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # if request.user.is_authenticated:
        #     user_id = request.user.id
        #     has_contacted = Contact.objects.filter(car_id=car_id, user_id=user_id)
        #     if has_contacted:
        #         messages.error(request, 'Ya has enviado una consulta sobre este automóvil. Por favor espera que nos pongamos en contacto.')
        #         return redirect('/cars/' + car_id)

        contact = Contact(
            car_id=car_id,
            car_title=car_title,
            car_price=car_price,
            user_id=user_id,
            first_name=first_name,
            last_name=last_name,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message
        )

        admin_info = User.objects.get(is_superuser=True)

        # Contacts email
        mail_subject = 'Solicitud de informacion sobre automovil'
        message = render_to_string('contacts/inquiry.html', {
            'user': admin_info,
            'car_title': car_title
        })
        to_email = admin_info.email
        send_email = EmailMessage(mail_subject, message, to=[to_email])
        send_email.send()

        contact.save()
        messages.success(request, 'Tu mensaje ha sido enviado exitosamente, serás contactado muy pronto.')
        return redirect('/cars/' + car_id)