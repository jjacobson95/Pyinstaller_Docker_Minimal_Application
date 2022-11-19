import sys
import docker
import os
import tarfile
import time
import platform
import pathlib
import threading
from multiprocessing import Pool
import multiprocessing
import io
import re


client = docker.from_env()
image = "python:3.9-bullseye"    


local_mem = os.getcwd() + "/test_area"
command_list = ["print('Hello World')"]


def process(nums):
    global client,image,local_mem,command_list
    cont_name = ("Test_container_" + str(nums))
    print("Preparing to run ", cont_name)
    client.containers.run(image,name=cont_name, detach=True, tty=True)
    print("Container started: ", cont_name)
    PW_container = client.containers.get(cont_name)
    PW_container.exec_run(cmd=command_list)    
    PW_container.stop()
    print("Container stopped: ", cont_name)
    time.sleep(2)
    PW_container.remove()


def run_container():
    global client,image,local_mem,command_list
    multiprocessing.freeze_support()
    nums = [1,2,3]
    process_num = len(nums)
    if process_num > 10:
        process_num = 10

    pool = Pool(processes=process_num)
    pool.map(process,nums)

    pool.close()
    pool.join()
    return local_mem
