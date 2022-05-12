# thread = a flow of execution. Like a separate order of instructions.
#          However, each thread takes a turn running to achieve cocurrency

# GIL = global interpreter lock, allows only one thread to hold the control
#       of the Python interpreter at any one time

# cpu bound = program/task spends most of it's time waiting for internal events (CPU intensive)
#             use multiprocessing

# io bound = program/task spends most of its time waiting for eternal events (user input, web scraping)
#            use multithreading

import threading
import time

def eat_breakfast():
    time.sleep(3)
    print("You have finished eating breakfast\n")

def drink_coffee():
    time.sleep(4)
    print("You have finished drinking coffee\n")
    
def do_hw():
    time.sleep(5)
    print("You have finished doing homework\n")
    
#threading.Thread(target=callable_object, args=object_param) = creating a thread
eat_thread = threading.Thread(target=eat_breakfast, args=())
eat_thread.start() #starting a thread
    
drink_thread = threading.Thread(target=drink_coffee, args=())
drink_thread.start() #starting a thread

study_thread = threading.Thread(target=do_hw, args=())
study_thread.start() #starting a thread

#thread_object.join() = joining the thread to the MainThread which mean the main thread has to wait for this thread to finishing running b4 it can run
eat_thread.join()

#threading.active_count() = return the number of threads currently alive
print(threading.active_count())

#threading.enumerate() = return a list of all threads currently alive
print(threading.enumerate())

print(time.perf_counter())

