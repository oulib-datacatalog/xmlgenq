from celery.task import task
from celery import states
from celery.exceptions import Ignore
#from celery.task.sets import TaskSet
#from dockertask import docker_task
from subprocess import call,STDOUT
import requests,os
import jinja2
#from pandas import read_csv
#Default base directory 
basedir=os.environ.get('CC_STATIC_DIR')
hostname=os.environ.get('CC_HOSTNAME')

@task()
def metadataTemplateCreation(data,templatename="maps.tmpl",outname=None):
    """
    Metadata XML creation

    args: data - data that corresponds to template.
    kwargs:
        templatename - Default = maps.tmpl (name of template must correspond to template added to github template directory)
        outname - Default = None Will change templatename to .xml or use outname provided

    Github repo: https://github.com/oulib-datacatalog/xmlgenq
    """ 
    
    task_id = str(metadataTemplateCreation.request.id)
    #create Result Directory
    resultDir = os.path.join(basedir, 'oulib_tasks/', task_id)
    os.makedirs(resultDir)
    # load template
    templateLoader = jinja2.FileSystemLoader( searchpath=os.path.dirname(os.path.realpath(__file__)) )
    templateEnv = jinja2.Environment( loader=templateLoader )
    template = template = templateEnv.get_template("templates/{0}".format(templatename))
    outputXML = template.render(data)
    if not outname:
        if "field_local_identifier" in data:
            outname = "{0}.xml".format(data["field_local_identifier"].replace(" ","_"))
        else:
            outname="{0}.xml".format(templatename.split('.')[0])
    with open(os.path.join(resultDir,outname),'w') as out:
        out.write(outputXML)
    return "{0}/oulib_tasks/{1}/{2}".format(hostname,task_id,outname)
