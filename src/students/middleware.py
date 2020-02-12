import time

from students.models import Logger


class MyMiddleware:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        time_start = time.time()

        response = self.get_response(request)
        admin_url = '/admin/'

        # if request.path.startswith(admin_url):
        #     diff = time.time() - time_start
        #
        #     Logger.objects.create(
        #         path=request.path,
        #         method=request.method,
        #         time_delta=diff,
        #         user_id=request.user.id,
        #         user_email=str(request.user)
        #     )

        return response
