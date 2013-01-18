from django.http import HttpResponse
from django.shortcuts import render_to_response
from books.models import Book
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
    return render_to_response('list_meta.html', {'list_meta': values})
    from django.shortcuts import render_to_response


def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append('Enter a search term.')
        elif len(q) > 20:
            errors.append('Please enter at most 20 characters.')
        else:
            books = Book.objects.filter(title__icontains=q)
            return render_to_response('search_results.html',
                {'books': books, 'query': q})
    return render_to_response('search_form.html',
        {'errors': errors})
