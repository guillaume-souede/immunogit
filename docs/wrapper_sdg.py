# sdg : attempt not to make .py files for each .ipynb in order to get "proper" autodoc
# this is a wrapper - like attempt : 
import types
import inspect
import os
from glob import glob
from nbformat import read
from nbconvert import PythonExporter

def load_notebook_as_module(path, module_name):
    with open(path, 'r', encoding='utf-8') as f:
        nb = read(f, as_version=4)
    code, _ = PythonExporter().from_notebook_node(nb)
    mod = types.ModuleType(module_name)
    exec(code, mod.__dict__)
    return mod

notebook_paths = glob(os.path.join(os.path.dirname(__file__), "../src/*.ipynb"))

for path in notebook_paths:
    module_name = os.path.splitext(os.path.basename(path))[0]
    mod = load_notebook_as_module(path, module_name)
    for name, obj in mod.__dict__.items():
        if inspect.isfunction(obj) or inspect.isclass(obj):
            globals()[name] = obj
            
# END