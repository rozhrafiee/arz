from celery import shared_task
from django.core.mail import send_mail
from .models import Currency

@shared_task
def check_currency_change(currency_id, alert_value):
    try:
        currency = Currency.objects.get(id=currency_id)
        daily_change = currency.daily_change

        if daily_change > alert_value:
            message = f"The daily change of {currency.name} is higher than {alert_value}!"
            send_mail(
                'Currency Alert',
                message,
                'mahansepanloooo@gmail.com.com',
                ['rozhinarafiee014@gmail.com.com'],
                fail_silently=False,
            )
        elif daily_change < alert_value:
            message = f"The daily change of {currency.name} is lower than {alert_value}!"
            send_mail(
                'Currency Alert',
                message,
                'mahansepanloooo@gmail.com.com',
                ['rozhinarafiee014@gmail.com.com'],
                fail_silently=False,
            )
        else:
            message = f"The daily change of {currency.name} is equal to {alert_value}!"
            send_mail(
                'Currency Alert',
                message,
                'mahansepanloooo@gmail.com.com',
                ['rozhinarafiee014@gmail.com.com'],
                fail_silently=False,
            )
    except Currency.DoesNotExist:
        print(f"Currency with id {currency_id} does not exist.")