from dj import settings


def template_settings(request):
    return {
        'ANALYTICS': getattr(settings, 'ANALYTICS', ''),
        'POPULAR': getattr(settings, 'POPULAR', [])
    }
