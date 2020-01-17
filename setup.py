#import ez_setup
#ez_setup.use_setuptools()
from setuptools import setup, find_packages
setup(name='xmlgenq',
      version='0.0',
      packages= find_packages(),
      package_data={'xmlgenq':['tasks/templates/*.tmpl','xmlgenq/tasks/templates/*.tmpl']},
      install_requires=[
          'pymongo==3.2.1',
          'requests==2.20.0',
          'jinja2',
      ],
     dependency_links=[
          'http://github.com/ouinformatics/dockertask/tarball/master#egg=dockertask-0.0',
      ],
     include_package_data=True,
)
