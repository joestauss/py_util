def autoprime_coroutine( coroutine):
    tmp = coroutine()
    tmp.send()
    return tmp
