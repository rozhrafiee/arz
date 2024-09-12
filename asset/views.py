from django.http.response import HttpResponse, JsonResponse, HttpResponseBadRequest
import json
import requests
from rest_framework.views import APIView

import requests
import json
from django.http import JsonResponse


def arz(request):
    src_currency = request.GET.get('srcCurrency', 'btc')
    dst_currency = request.GET.get('dstCurrency', 'rls')

    url = f'https://api.nobitex.ir/market/stats?srcCurrency={src_currency}&dstCurrency={dst_currency}'
    response = requests.get(url)



    if response.status_code == 200:
        data = json.loads(response.content)
        d = {
            "ghaymat":data['stats'][f'{src_currency}-{dst_currency}']['latest'],
            "dayChange":data['stats'][f'{src_currency}-{dst_currency}']['dayChange']
        }
        return JsonResponse(data=d, safe=False)
    else:
        return JsonResponse({'error': 'Failed to retrieve data'}, status=response.status_code)

