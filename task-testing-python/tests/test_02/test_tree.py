from tree_utils_02.tree import Tree
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

@pytest.mark.parametrize(
    ['a', 'b',  'answer'], [
        (False, False, ''),
        (False, True, ''),
        (True, False, ''),
        (True, True, '')
    ])
def test_get(files, a, b, answer):
    assert answer == Tree().get(test_path, dirs_only=a, recurse_call=b).name


def test_construct_filenode(files):
    assert '' == Tree().construct_filenode(test_path, is_dir=True).name


def test_get2(files):
    assert '' == Tree().get(test_path, dirs_only=True, recurse_call=True).name


def test_error_path():
    with pytest.raises(AttributeError):
        Tree().get('./error', dirs_only=False, recurse_call=True)


def test_not_dir(files):
    with pytest.raises(AttributeError):
        Tree().get(test_path + '1.txt', dirs_only=True, recurse_call=False)


def test_filter_empty_nodes(files):
    assert None == Tree().filter_empty_nodes(
        FileNode(name='1.txt', is_dir=False, children=[]))


def test_filter_empty_nodes2(files):
    with pytest.raises(ValueError):
        Tree().filter_empty_nodes(FileNode(name='5', is_dir=True, children=[]))


def test_filter_empty_nodes3(files):
    filenode_inner = FileNode(name='3\\4', is_dir=True, children=[])
    filenode_outer = FileNode(name='3', is_dir=True, children=[filenode_inner])

    assert None == Tree().filter_empty_nodes(filenode_outer, current_path=test_path)