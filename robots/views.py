import json
from datetime import timedelta

from django.http import HttpResponse, JsonResponse
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_GET, require_POST

from constants import CONTENT_TYPE, RobotMessages
from .forms import RobotForm
from .utils import create_excel_file, fetch_robot_data


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


@require_GET
def generate_report(request):
    """Генерация отчета и возврат файла."""
    now = timezone.now()
    last_week = now - timedelta(days=7)

    models_data = fetch_robot_data(last_week)
    wb = create_excel_file(models_data)

    response = HttpResponse(content_type=CONTENT_TYPE)
    filename = f'report_{last_week.strftime('%Y-%m-%d %H:%M')}.xlsx'
    response['Content-Disposition'] = f'attachment; filename={filename}'
    wb.save(response)

    return response
