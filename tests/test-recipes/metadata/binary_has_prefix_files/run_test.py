import os

prefix = os.environ['PREFIX']
fn = os.path.join(prefix, 'binary-has-prefix')

with open(fn, 'rb') as f:
    data = f.read()

print(data)
assert prefix.encode('utf-8') in data
