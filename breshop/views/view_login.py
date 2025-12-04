from django.http import JsonResponse
from django.contrib.auth import authenticate, login
import json
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    if request.method != "POST":
        return JsonResponse({'error': 'Post required'}, status=400)
    
    data = json.loads(request.body)
    user = authenticate(
        request,
        username = data.get('username'),
        password = data.get('senha')
    )

    if user is None:
        return JsonResponse({'erro': 'credenciais invalida'}, status=400)
    
    login(request, user)

    return JsonResponse({'mensagem': 'Loggin realizado'}, status=200)

def me_view(request):
    if not request.user.is_authenticated:
        return JsonResponse({'is_authenticated': False}, status=401)
    
    return JsonResponse({
        "username": request.user.username,
        "is_superuser": request.user.is_superuser,
        "is_staff": request.user.is_staff
    })
