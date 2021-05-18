def autoprime( coroutine):
    tmp = coroutine()
    tmp.send( None)
    return tmp
