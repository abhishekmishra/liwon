"""
PyBuilder build file for "liwon"

Author: Abhishek Mishra (abhishekmishra3@gmail.com)
Date: 07/05/2018

"""

from pybuilder.core import use_plugin, init, Author

use_plugin('python.core')
use_plugin('python.install_dependencies')
use_plugin("python.distutils")

name = 'liwon'
authors = [Author('Abhishek Mishra', 'abhishekmishra3@gmail.com')]
license = 'GPL3'
summary = 'liwon: Learning in Wonderland'
url = 'https://github.com/abhishekmishra/liwon'
version = '0.0.1'

default_task = 'publish'

@init
def initialize (project):
    project.depends_on_requirements("requirements.txt")