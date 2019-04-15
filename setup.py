""" 
Pygments stuff for the style
""" 
from setuptools import setup, find_packages

setup( 
    name         = 'pygments-blackened',
    version      = '1.0',
    description  = __doc__,
    author       = "Kurt Böhm",
    install_requires = ['pygments'],
    packages     = find_packages(),
    entry_points = '''
    [pygments.styles]
    blackened = pygments_blackened.style:BlackenedStyle
    '''
)
