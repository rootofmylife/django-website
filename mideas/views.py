#!/usr/bin/env python3
#-*- coding: utf-8 -*-

from django.shortcuts import render
from django.http import Http404, HttpResponse
from django.http import HttpResponseRedirect
import csv
from django.http import StreamingHttpResponse
import nltk
import codecs

def home(request):
    if request.method == "POST":      
        for f in request.FILES.getlist('files'):
            if f.name == 'key.txt':
                keys = f.read().splitlines()
            elif f.name == 'mess.txt':
                mess = f.read().splitlines()

        keys = [s.decode() for s in keys]
        mess = [s.decode() for s in mess]
	
	
        del keys[0]
        del mess[0]
        rs = []
        sym = r"~`!@#$%^&*()_-+=[]{}|;':\"”“,./<>?"
        keys = [s.translate({ord(c): "" for c in sym}) for s in keys]
        mess = [s.translate({ord(c): "" for c in sym}) for s in mess]
        mess = [s.strip() for s in mess if s != 'NULL']
        mess = [str(s) for s in mess]

        keys = ' '.join(keys)
        keys = keys.split()

        mess = ' '.join(mess)
        mess = list(set(mess.split()))
        for i in keys:
                temp = []
                temp.append(i)
                for j in mess:
                        if i in j:
                                temp.append(j)
                        temp_dv = nltk.edit_distance(i.lower(), j.lower())
                        if temp_dv < (len(i) - (len(i) * 0.5)) and temp_dv > 0:
                                temp.append(j)
                rs.append(temp)
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="somefilename.csv"'
        response.write(codecs.BOM_UTF8)
        writer = csv.writer(response)

        for i in rs:
            writer.writerow(i)
            writer.writerow('\n')
	
        return response

    return render(request,'mideas/home.html')
