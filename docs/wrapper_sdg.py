import types
import inspect
from pathlib import Path
from nbformat import read

def load_notebook_as_module(nb_path: Path):
    module_name = nb_path.stem
    
    with open(nb_path, 'r', encoding='utf-8') as f:
        nb = read(f, as_version=4)
    
    # Extract only code cells to avoid nbconvert overhead
    code_cells = [c.source for c in nb.cells if c.cell_type == 'code']
    source_code = "\n\n".join(code_cells)
    
    mod = types.ModuleType(module_name)
    mod.__file__ = str(nb_path)
    
    # Execute in the module's dict so it behaves like a real module
    exec(source_code, mod.__dict__)
    return mod

# Configuration
base_dir = Path(__file__).parent.parent / "src"
notebook_paths = base_dir.glob("*.ipynb")

for path in notebook_paths:
    try:
        mod = load_notebook_as_module(path)
        
        # Filter for objects actually defined in the notebook 
        # (prevents re-importing things imported inside the notebook)
        for name, obj in inspect.getmembers(mod):
            if inspect.isfunction(obj) or inspect.isclass(obj):
                if obj.__module__ == mod.__name__:
                    globals()[name] = obj
    except Exception as e:
        print(f"Failed to load notebook {path.name}: {e}")
