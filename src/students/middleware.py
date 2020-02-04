from datetime import datetime

from students.models import Logger


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        time_start = datetime.now()

        response = self.get_response(request)

        if request.path.find('admin/') != -1:
            # print('MIDDLEWARE' * 10)
            # print('MIDDLEWARE' * 10)
            # print('MIDDLEWARE' * 10)
            # print('MIDDLEWARE' * 10)
            log = Logger.objects.create(
                path=request.path,
                method=request.method,
                time_delta=str(datetime.now() - time_start),
                user_id=request.user.id,
                user_email=str(request.user)
            )
            log.save()

        return response
