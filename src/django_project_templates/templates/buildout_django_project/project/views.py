from django.contrib.auth import login
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template.context import RequestContext
#from registration import signals
from pages.views import details
from vdr.views import plans

def registration_activation_complete_callback(sender, **kwargs):
    user = kwargs['user']
    request = kwargs['request']
    backend = ModelBackend
    user.backend = 'django.contrib.auth.backends.ModelBackend'
    login(request, user)
#signals.user_activated.connect(registration_activation_complete_callback)


@login_required
def post_login_handler(request):

    user = request.user

    try:
        profile_obj = user.get_profile()
    except ObjectDoesNotExist:
        return HttpResponseRedirect(reverse("profiles_create_profile"))

    if not user.email or not user.first_name or not user.last_name:
        return HttpResponseRedirect(reverse("profiles_complete_profile"))

    if profile_obj.location is None or not profile_obj.location.city:
        return HttpResponseRedirect(reverse("profiles_complete_profile"))

    return HttpResponseRedirect("/")


def index_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect(reverse("browse-folder"))
    return plans(request)

def handler500(request, template_name='500.html'):
    """
    500 error handler.

    Templates: `500.html`
    Context: None
    """
    return render_to_response(template_name,
        context_instance = RequestContext(request)
    )