


class Cart():
    def __init__(self, request):
        self.session = request.session

        # Get the current session key if exist
        cart = self.session.get('session_key')

        # If the user is new and no session , Create One
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}


        # Make sure cart is available all pages
        self.cart = cart

