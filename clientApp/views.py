from django.http import HttpResponse
from django.shortcuts import render_to_response
import json
from django.http import HttpResponse

#Return template for contacts
def load_contact(request):
	return render_to_response('contact.html')


#TODO: try insert  
def create_data(request):
	
	if request.method == 'POST':
		return HttpResponse(
		    json.dumps({"nsiii ": "siiiiii"}),
		    content_type="application/json"
		)
		name = request.POST.get('param')
		response_data = {}


		#(first_name='dasd', last_name='')
		data = Client(first_name=name)
		var = Client.objects.create(data)
		var.save()

		response_data['result'] = 'Create successful!'

		return HttpResponse(
	        json.dumps(response_data),
	        content_type="application/json"
	    )
	else:
		return HttpResponse(
		    json.dumps({"ERROR": "Error - not insert"}),
		    content_type="application/json"
		)
	



