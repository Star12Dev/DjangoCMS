from django.http import JsonResponse
from django.shortcuts import render


# loggin Details#
import logging

# Start Logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# create a file handler
handler = logging.FileHandler('log_terminal.log')
handler.setLevel(logging.DEBUG)
# create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)
# add the handlers to the logger
logger.addHandler(handler)

def log_checker(request):
    dashboard = request.POST['dashboard']
    author = request.POST['author']

    file_name = 'resources/user_logs/' + author + dashboard + ".log"
    #logger.info(file_name)

    with open(file_name, 'r') as f:
        lines = f.read().splitlines()
        if len(lines) > 0:
            #TODO: Use the model to display the number of desired lines
            last_line = lines[-100:]
            logs = ''
            for i in last_line:
                logs += i+'\n'
            logfile = logs


        else:
            logfile = 'No logs found!'



    return JsonResponse({'logfile': logfile, 'id': author + dashboard})
