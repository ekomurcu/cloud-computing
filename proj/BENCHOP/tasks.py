from celery import Celery
from oct2py import octave
from oct2py import Oct2Py
import os

app = Celery('tasks', backend='rpc://', broker='pyamqp://guest@localhost//')

@app.task
def tupling(x):
    l= [x,x]
    return tuple(l)
@app.task
def add(x,y ):
    return {"x": x, "y": y, "sum": x+y}
@app.task
def benchop(x):
    oc = Oct2Py()
#    time, relerr = oc.feval("Table_run", 1)

    time, relerr = oc.Table_run(x, nout=2)
    time_flat = []
    for sublist in time:
        for item in sublist:
            time_flat.append(item)
    relerr_flat = []
    for sublist in relerr:
        for item in sublist:
            relerr_flat.append(item)


    return (time_flat, relerr_flat)




#    return  {z[0]:list(z[1:]) for z in zip(time_flat, relerr_flat)} #TODO SKRIV OM
