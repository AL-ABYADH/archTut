from django.utils.deprecation import MiddlewareMixin

class CustomMiddleware(MiddlewareMixin):
    def process_request(self, request):
        # Add custom logic before the view is called
        if request.path.startswith('/books/'):
            print("Custom middleware logic for books view")

    def process_response(self, request, response):
        # Add custom logic after the view is called
        if request.path.startswith('/books/'):
            print("Custom middleware logic for books view response")
        return response
