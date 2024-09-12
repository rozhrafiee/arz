from django.http import JsonResponse
from rest_framework.views import APIView
from .models import Alarm
import requests
import json


def arz(request):
    src_currency = request.GET.get('srcCurrency', 'btc')
    dst_currency = request.GET.get('dstCurrency', 'rls')


    url = f'https://api.nobitex.ir/market/stats?srcCurrency={src_currency}&dstCurrency={dst_currency}'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        if f'{src_currency}-{dst_currency}' in data['stats']:
            exchange_data = data['stats'][f'{src_currency}-{dst_currency}']
            d = {
                "ghaymat": exchange_data['latest'],
                "dayChange": exchange_data['dayChange']
            }
            return JsonResponse(data=d, safe=False)
        else:
            return JsonResponse({'error': f'No data available for {src_currency}-{dst_currency}'}, status=404)
    else:
        return JsonResponse({'error': 'Failed to retrieve data'}, status=response.status_code)


class Allarm(APIView):
    def post(self, request):
        data = request.data

        name = data.get('name')
        price = data.get('price')
        up_or_downe = data.get('v')

        if not name or price is None or up_or_downe is None:
            return JsonResponse({'error': 'Name, price, and up_or_downe are required.'}, status=400)


        Alarm.objects.create(name=name, price=price, up_or_downe=up_or_downe)

        return JsonResponse({'message': 'Alarm created successfully!'}, status=201)