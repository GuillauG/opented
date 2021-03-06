import os
from itertools import count
from lxml import html


def tender_path(year, num, tab, create=True):
    hash_dir = int(str(num)[:3])
    path = 'tenders/%s/%03d/%s/tab_%s.html' % (year, hash_dir, num, tab)
    dirname = os.path.dirname(path)
    if create and not os.path.isdir(dirname):
        os.makedirs(dirname)
    return path

def generate_paths(year, num):
    path = tender_path(year, num, 0, create=False)
    if not os.path.isfile(path):
        return None
    dir_base = os.path.dirname(path)
    pattern = dir_base + '/tab_%s.html'
    return [pattern % i for i in range(0, 4)]

def traverse_local():
    for year in range(2009, 2014):
        for num in count(1):
            paths = generate_paths(year, num)
            if paths is None:
                break
            yield paths

def as_document(path):
    try:
        fh = open(path, 'rb')
        doc = html.fromstring(fh.read().split('\r\n', 1)[-1])
        fh.close()
        return doc
    except IOError:
        return None


