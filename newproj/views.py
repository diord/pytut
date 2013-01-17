from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime

def hello(request):
    return HttpResponse("hello!!!")

def current_datetime(request):
	now = datetime.datetime.now()	
	html = "<html><body>It is now %s.</body></html>" % now 
	return HttpResponse(html)

def hours_ahead_old(request, offset):
	try: 
		offset = int(offset)
	except VlalueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)	
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt) 
	return HttpResponse(html)	

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	return render_to_response('hours_ahead.html', {'hours_offset': offset, 'next_time': dt})

def about(request):
	html = "<html><body>version %s.</body></html>" % 0.1 
	return HttpResponse(html)

def display_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    for k, v in values:
        html.append('<tr><td>%s</td><td>%s</td></tr>' % (k, v))
    return HttpResponse('<table>%s</table>' % '\n'.join(html))