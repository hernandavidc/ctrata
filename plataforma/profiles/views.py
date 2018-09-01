from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.http import Http404, JsonResponse

from registration.models import Profile


# Create your views here.
class ProfileListView(ListView):
    model = Profile
    template_name = 'profiles/profile_list.html'
    paginate_by = 8

def ProfileDetailApiView(request, dni):
    userReturn = get_object_or_404(Profile, dni=dni)
    json_responder = {
        'username':userReturn.user.username,
        'name':userReturn.user.first_name,
        'apellidos':userReturn.user.last_name,
        'pais':userReturn.ciudad.pais.name,
        'ciudad':userReturn.ciudad.name,
        'tipo':userReturn.typeProfile,
    }
    return JsonResponse(json_responder)

class ProfileDetailView(DetailView):
    model = Profile
    template_name = 'profiles/profile_detail.html'

    def get_object(self):
        return get_object_or_404(Profile, user__username=self.kwargs['username'])
