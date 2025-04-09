from django.http import JsonResponse

def api_root(request):
    return JsonResponse({
        "message": "Bem-vindo ao Octofit API!",
        "codespace_url": "https://[zany-space-zebra-4675vp697x627qpr]-8000.app.github.dev",
        "localhost_url": "http://localhost:8000"
    })