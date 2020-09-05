from django.shortcuts import render
from tablodene.models import Denemetablo
# Create your views here.
def home_view(request):
	data={}
	x=Denemetablo.objects.all()
	for i in x:
		data[i.id]={
			'myint':i.rand_int,
			'mystr':i.rand_str
		}
	tmpdata={'mydata':data}
	return render(request,"home.html",tmpdata)