"""
Write a synchronous function that makes a directory and
recursively makes all of its parent directories as necessary.

A directory is specified via a sequence of arguments which specify the path. For example:

mkdirp('/','tmp','made','some','dir')

...will make the directory /tmp/made/some/dir.

Like the shell command mkdir -p,
the function you program should be idempotent if the directory already exists.
"""


def mkdirp(*directories):
    import os

    dir_path = ""
    for dir_elem in directories:
        dir_path = os.path.join(dir_path, dir_elem)

        if not os.path.exists(dir_path):
            os.mkdir(dir_path)

from unittest import TestCase


class TestMkdir(TestCase):
    def test_mkdir(self):
        mkdirp("C:", "/tmp", "directories", "can", "be", "made", "recursively")

        self.assertTrue(
            os.path.exists('C:/tmp/directories/can/be/made/recursively'),
            '/tmp/directories/can/be/made/recursively does not exist')