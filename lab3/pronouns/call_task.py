from tasks import add
result= add.delay(4,4)
#print(result.ready())
#print(result.get(timeout=1))
#result.get(propagate=False)
#result.traceback
for v in result.collect():
    print(v)

