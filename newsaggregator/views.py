from django.shortcuts import render
from . import utils

# bd govt jobs
bdgovt = utils.bdgovtjob()

############################################################
telebd = utils.telebd()

# Create your views here.
def home(request):


    return render(request, 'home.html', {'bdgovtjobs': bdgovt, 'telejobs': telebd})