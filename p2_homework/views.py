from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect, Http404
from django.core.urlresolvers import reverse
from django.core.context_processors import csrf

from p2_homework.models import Document
from p2_homework.forms import DocumentForm

import json


def list(request):
	"""Upload files and return list of Document files"""
	request.session['upload_session'] = 'Otwarcie sesji.'
	upload_session = request.session['upload_session']
	
	# Handle file upload
	if request.method == 'POST':
		
		form = DocumentForm(request.POST, request.FILES)
		if form.is_valid():
			newdoc = Document(docfile = request.FILES['docfile'])
			newdoc.save()
		del request.session['upload_session']
		
		# Redirect to the document list after POST
		return HttpResponseRedirect(reverse('p2_homework.views.list'))
	else:
		form = DocumentForm()
	
	# Load documents for the list page	
	documents = Document.objects.all()
	
	# Render list page with the documents and the form
	return render_to_response(
	    'list.html',
	    {'documents': documents, 'form': form, 'upload_session': upload_session},
	    context_instance=RequestContext(request))



def specific_document(request, document_id):
	"""Returns and renders specific Document file"""
	try:
		with open('/home/bartek/Pulpit/new_project/files/'+str(Document.objects.get(id=document_id).docfile.name), 'r') as json_file:
			mydata = json.loads(json_file.read())
			
		document = Document.objects.get(id=document_id)
		
	except Document.DoesNotExist:
		raise Http404
	return render_to_response('specific_document.html', {"mydata": mydata, "document": document},)

def edit(request, document_id):
    """Edit Document file from POST data"""
    try:
        document = Document.objects.get(id=document_id)
    except Document.DoesNotExist:
        raise Http404
    with open('/home/bartek/Pulpit/new_project/files/'+str(document.docfile.name), 'r+') as json_file:
        mydata = json.loads(json_file.read())
        # Handled uploaded data to edited file
        if request.method == 'POST':
			# Set the uploaded data as a value of the .json file key
            for key in mydata:
                mydata[key] = request.POST.get('content', '')

            # Move the position to the begnning of the file
            json_file.seek(0)
            # Write object as JSON
            json_file.write(json.dumps(mydata))
            # Truncate excess file contents
            json_file.truncate()
            
            args = {}
            args['mydata'] = mydata
            args.update(csrf(request))
            return HttpResponseRedirect('/specific_document/%s' % document_id, args)
        else:
            with open('/home/bartek/Pulpit/new_project/files/'+str(document.docfile.name), 'r') as json_file:
                mydata = json.loads(json_file.read())
                
            args = {}
            args['mydata'] = mydata
            args.update(csrf(request))
    
            return render_to_response('edit.html', args)
