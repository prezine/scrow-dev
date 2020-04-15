from django.http import HttpResponseRedirect


class AuthOnlyMiddleware:
    def process_request(self, request):
        if not request.user.is_authenticated:
            return HttpResponseRedirect('/')

        return None


class AuthUserOnlyMiddleware:
    def process_request(self, request):
        if request.user.is_authenticated:
            if not request.user.is_staff:
                return None
            return HttpResponseRedirect('/admin')
        else:
            return HttpResponseRedirect('/login')


class NonAuthMiddleware(object):
    def process_request(self, request):
        if request.user.is_authenticated:
            if request.user.is_staff:
                return HttpResponseRedirect('/admin')
            return HttpResponseRedirect('login')
        return None


class BusinessOnlyMiddleware:
    def process_request(self, request):
        if request.user.is_authenticated:
            if request.user.active_business:
                return None
            elif not request.user.is_staff:
                return HttpResponseRedirect('/getting-started')
            return HttpResponseRedirect('/admin')
        else:
            return HttpResponseRedirect('/login')
