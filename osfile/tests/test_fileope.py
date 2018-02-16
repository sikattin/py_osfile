# -*- coding: utf-8 -*-
import unittest
import zipfile
import tempfile
import stat
from osfile import fileope

TESTDIR_PATH = '/tmp/test/test1/test2/test3'
TESTDIR_BASE = '/tmp/test'
class TestFileope(unittest.TestCase):
    """fileope module test class."""

    def setUp(self):
        """entering process."""
        if not fileope.dir_exists(path=TESTDIR_PATH):
            fileope.make_dirs(path=TESTDIR_PATH)

    def tearDown(self):
        """exiting process"""
        pass

    def test_zip_data(self):
        """zip_data function test method."""
        fileope.zip_data(file_path=TESTDIR_PATH)
        self.assertTrue(zipfile.is_zipfile("{}.zip".format(TESTDIR_BASE)))

    def test_add_write_permissions(self):
        with tempfile.NamedTemporaryFile() as fobj:
            # test add write permission to group target.
            fileope.add_write_permissions(path=fobj.name,
                                          target='g')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '620', msg="mode: {}".format(mode))
            # test add write permission to other target.
            fileope.add_write_permissions(path=fobj.name,
                                          target='o')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '622', msg="mode: {}".format(mode))
        del fobj

        with tempfile.NamedTemporaryFile() as fobj:
            # test add write permission to all target.
            fileope.add_write_permissions(path=fobj.name,
                                          target='a')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '622', msg='mode: {}'.format(mode))


    def test_add_read_permissions(self):
        with tempfile.NamedTemporaryFile() as fobj:
            # test add read permission to group target.
            fileope.add_read_permissions(path=fobj.name,
                                          target='g')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '640', msg="mode: {}".format(mode))
            # test add read permission to other target.
            fileope.add_read_permissions(path=fobj.name,
                                          target='o')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '644', msg="mode: {}".format(mode))
        del fobj

        with tempfile.NamedTemporaryFile() as fobj:
            # test add read permission to all target.
            fileope.add_read_permissions(path=fobj.name,
                                          target='a')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '644', msg='mode: {}'.format(mode))

    def test_add_exc_permissions(self):
        with tempfile.NamedTemporaryFile() as fobj:
            # test add exc permission to user target.
            fileope.add_exc_permissions(path=fobj.name,
                                          target='u')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '700', msg="mode: {}".format(mode))
            # test add exc permission to group target.
            fileope.add_exc_permissions(path=fobj.name,
                                          target='g')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '710', msg="mode: {}".format(mode))
            # test add exc permission to other target.
            fileope.add_exc_permissions(path=fobj.name,
                                        target='o')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '711', msg="mode: {}".format(mode))
        del fobj

        with tempfile.NamedTemporaryFile() as fobj:
            # test add write permission to all target.
            fileope.add_exc_permissions(path=fobj.name,
                                          target='a')
            mode = oct(stat.S_IMODE(os.stat(fobj.name).st_mode))[2:]
            self.assertEqual(mode, '711', msg='mode: {}'.format(mode))


if __name__ == '__main__':
    unittest.main()