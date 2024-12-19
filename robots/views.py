import json

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST

from constants import RobotMessages
from .forms import RobotForm


@csrf_exempt
@require_POST
def create_robot(request):
    try:
        data = json.loads(request.body)
    except json.JSONDecodeError:
        return JsonResponse({
            'error': RobotMessages.ERROR_INVALID_JSON
        }, status=400)

    form = RobotForm(data)

    if form.is_valid():
        robot = form.save(commit=False)
        robot.serial = f'{robot.model}-{robot.version}'
        robot.save()
        return JsonResponse(
            {
                'message': RobotMessages.SUCCESS_CREATE.format(
                    serial=robot.serial
                )
            }, status=201)
    else:
        return JsonResponse({'errors': form.errors}, status=400)
