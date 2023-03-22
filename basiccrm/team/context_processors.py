from .models import Team


def activ_team(request):
    if request.user.is_authenticated:
        activ_team = Team.objects.filter(created_by=request.user)[0]
    else:
        activ_team = None

    return {'activ_team': activ_team}
