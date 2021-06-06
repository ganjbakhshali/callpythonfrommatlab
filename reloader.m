function reloader(module)
clear module
mod=py.importlib.import_module(module);
py.importlib.reload(mod)

end