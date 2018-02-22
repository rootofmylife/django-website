from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.shortcuts import render
from .models import FileUpload, UploadForm
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
import csv
from django.http import StreamingHttpResponse

class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


def home(request):
    if request.method == "POST":

        #for f in request.FILES.getlist('files'):
        #    filename = f.name
        #    listname.append(filename)
        #file = request.FILES.getlist('files')
        
        for f in request.FILES.getlist('files'):
            if f.name == 'key.txt':
                key = f.read().splitlines()
            elif f.name == 'mess.txt':
                mess = f.read().splitlines()
        

        key = [s.decode() for s in key]
        mess = [s.decode() for s in mess]
        


        del key[0]
        del mess[0]
        rs = []

        rs.append(key)
        rs.append(mess)
        
        '''
        pseudo_buffer = Echo()
        writer = csv.writer(pseudo_buffer)
        response = StreamingHttpResponse((writer.writerow(r.decode('utf-8')) for r in rs),
                                     content_type="text/csv")
        response['Content-Disposition'] = 'attachment; filename="output.csv"'
        '''
        
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'

        writer = csv.writer(response)

        for i in rs:
            writer.writerow(i)
            writer.writerow('\n')


        return response
        
        #return HttpResponse(str(rs[0]))

    return render(request,'mideas/home.html')