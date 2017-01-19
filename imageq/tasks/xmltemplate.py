from celery.task import task
from celery import states
from celery.exceptions import Ignore
from celery.task.sets import TaskSet
#from dockertask import docker_task
from subprocess import call,STDOUT
import requests
import os, hashlib, bagit
from pymongo import MongoClient
import boto3,shutil
import jinja2
#from pandas import read_csv
#Default base directory 
basedir="/data/web_data/static"

@task()
def metadataTemplateCreation(data,templatename="maps.tmpl"):
    task_id = str(metadataTemplateCreation.request.id)
    #create Result Directory
    resultDir = os.path.join(basedir, 'oulib_tasks/', task_id)
    os.makedirs(resultDir)
    # load template
    templateLoader = jinja2.FileSystemLoader( searchpath="/" )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = template = templateEnv.get_template("template/{0}".format(templatename))
    outputXML = template.render(data)
    with open(os.path.join(resultDir,"mytemplate.xml"),'w') as out:
        out.write(outputXML)
    return "http://dev.libraries.ou.edu/oulib_tasks/{0}".format(task_id)
