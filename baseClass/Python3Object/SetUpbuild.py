"""
setup.py
"""
 
from distutils.core import setup, Extension
 
 
People_module = Extension('_People',
                           sources=['People.cpp','People_wrap.cxx'],
#                           version ='0.1',
#                           author = 'Concyclics',
#                           description = """Simple swig example from docs""",
#                           py_modules = ["People"],
                           )
 
setup (name = 'People',
       version = '0.1',
       author      = "Concyclics",
       description = """Simple swig example from docs""",
       ext_modules = [People_module],
       py_modules = ["People"],
       )