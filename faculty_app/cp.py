from .models import Departmant


def list_dp(request):
    return {"list_dp": Departmant.objects.all()}
