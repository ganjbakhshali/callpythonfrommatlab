clear classes
a=[2 8;7 2;15 33;29 4];
mod = py.importlib.import_module('factorMUL');
py.importlib.reload(mod);
p=py.factorMUL.mul(a(:,1),a(:,2));
factorMUL = double(py.array.array('d',py.numpy.nditer(p(1))))
vars=