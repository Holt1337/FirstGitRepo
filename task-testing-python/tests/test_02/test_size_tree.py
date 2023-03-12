from tree_utils_02.size_tree import SizeTree
from tree_utils_02.size_node import FileSizeNode
from tree_utils_02.node import FileNode

import os
import pytest
import shutil



FILES = ['1.txt', '2.txt']
DIRS = ['3', '3/4']

test_path = './tests/test_02/0/'

@pytest.fixture(scope='module')
def files():
    os.mkdir( test_path)
    for filename in FILES:
        open(test_path + filename, 'w')
    for dir in DIRS:
        os.mkdir(test_path + dir)
    yield  DIRS

    # teardown
    shutil.rmtree(test_path)


def test_get_children_tree(files):
    assert [] == SizeTree().construct_filenode( test_path, is_dir=True).children

def test_get_children_tree2(files):
    assert [] == SizeTree().construct_filenode( test_path, is_dir=False).children

def test_update_filenode(files):
    filenode_inner = FileNode(name='3\\4', is_dir=True, children=[])
    filesize_inner = FileSizeNode(filenode_inner, is_dir=True, children=[], size=0)

    filenode_outer = FileNode(name='3', is_dir=True, children=[])
    filesize_outer = FileSizeNode(filenode_outer, is_dir=False,
                                  children=[filesize_inner], size=0)
    assert 0 == SizeTree().update_filenode(filesize_outer).size
