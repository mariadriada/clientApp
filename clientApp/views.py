#Need for send template 
from django.shortcuts import render_to_response

#Return template for contacts
def load_contact(request):
	return render_to_response('contacts.html')

