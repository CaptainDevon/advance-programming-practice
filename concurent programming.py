from time import sleep
from multiprocessing import Process
 

def task():
    sleep(1)
    print('This is coming from another process', flush=True)
 

if __name__ == '__main__':
    
    process = Process(target=task)
   
    process.start()
    
    print('Waiting for the new process to finish...')
   
    process.join()



print("Name:Divyansh Sinha")
print("RegNo:RA2111026030117")
print("section:C")

