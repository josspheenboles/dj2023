from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.
#view method(httprequest)--->return HttpResponse
def List(r):
   '''
    print(type(r))
    print(r)
    print(r.GET)
   '''
   # return HttpResponse('Catagory List')
   context={}
   context['username']='Asd@yahoo.com'
   return render(r,'index.html',context)


def Add(req):
    return HttpResponse('Catagroy Add')

def Update(req,catgid):
    '''
    print(req.method)
    print(req.GET)
    print(req.POST)
    print(req.path)
    print(req.META)

    print(req.get_host())
    print(catgid,type(catgid))
    '''
    resp=HttpResponse('hi</br>')
    resp.write('<h1>Hi</h1>')
    resp['content-type']='text/plain'
    resp.set_cookie('brnach','sohge')
    resp.set_cookie('track','web using python')
    return  resp
    #return HttpResponse('Catagory update'+str(catgid))