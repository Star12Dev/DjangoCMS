from task_tracker.models import *
from django.http.response import HttpResponse, JsonResponse
from urllib.parse import parse_qs
from django.views.decorators.csrf import csrf_exempt

# loggin Details#
import logging

# Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('task_tracker.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)



@csrf_exempt
def create_task(request):
    model_id = request.POST['model_id']
    active_task_holder = TaskHolder.objects.get(pk=model_id)

    try:
        new_task=TaskDetail.objects.create(model=active_task_holder)
        logger.debug('task created')

    except Exception as e:
        logger.exception("error from ajax")

    return JsonResponse(new_task.pk, safe=False)

@csrf_exempt
def delete_task(request):




    try:

        logger.debug(request.POST['task_id'])
        task_id = request.POST['task_id']
        active_task = TaskDetail.objects.get(pk=task_id)
        active_task.delete()
        logger.debug('task deleted')

    except Exception as e:
        logger.exception("error from ajax")

    return JsonResponse(task_id, safe=False)


@csrf_exempt
def save_task(request):
    try:


        task_id = request.POST['task_id']
        logger.debug(task_id)
        task_type=request.POST['task_type']
        task_value=request.POST['task_value']
        active_task = TaskDetail.objects.get(pk=task_id)
        if task_type=='Content':
            active_task.task_body=task_value

        else:
            active_task.task_title=task_value

        logger.debug(task_type)
        logger.debug(task_value)
        active_task.save()

        #active_task.task_body
        logger.debug('task saved')

    except Exception as e:
        logger.exception("error from ajax")

    return JsonResponse(task_id, safe=False)


@csrf_exempt
def complete_task(request):




    try:

        logger.debug(request.POST['task_id'])
        task_id = request.POST['task_id']
        active_task = TaskDetail.objects.get(pk=task_id)
        active_task.is_complete=True
        active_task.date_completed=datetime.now().date()
        active_task.save()
        logger.debug('task completed')

    except Exception as e:
        logger.exception("error from ajax")

    return JsonResponse(task_id, safe=False)

@csrf_exempt
def filter_outstanding(request):




    try:


        model_id = request.POST['model_id']
        filter_status = request.POST['filter_status']
        active_task_holder = TaskHolder.objects.get(pk=model_id)
        logger.debug(filter_status)
        if filter_status=='True':
            logger.debug("OK")
            active_task_holder.only_completed=False
        else:
            logger.debug("SDFDS")
            active_task_holder.only_completed=True

        active_task_holder.save()
        logger.debug('Filter Applied')

    except Exception as e:
        logger.exception("error from ajax")

    return JsonResponse(model_id, safe=False)
