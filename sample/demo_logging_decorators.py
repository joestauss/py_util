import time
import random
from py_util.decorators import record_function_calls, time_this

@time_this()
@record_function_calls()
def wait_a_bit( sleep_time):
    time.sleep( sleep_time)
    return f"I waited for {sleep_time} seconds."

@record_function_calls()
def zzz_different_function( ):
    return 7

if __name__ == "__main__":
    for _ in range( 5):
        wait_a_bit( random.random())
        zzz_different_function()
