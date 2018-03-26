# -*- coding: utf-8 -*-
import unittest
import zipfile
import tempfile
import os
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

    def test_change_write_permissions(self):
        with tempfile.NamedTemporaryFile() as fobj:
            # test change write permission to group target.
            fileope.change_write_permissions(path=fobj.name,
                                          target='g')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '020', msg="mode: {}".format(mode))
            # test change write permission to other target.
            fileope.change_write_permissions(path=fobj.name,
                                          target='o')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '002', msg="mode: {}".format(mode))
        del fobj

        with tempfile.NamedTemporaryFile() as fobj:
            # test change write permission to all target.
            fileope.change_write_permissions(path=fobj.name,
                                          target='a')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '222', msg='mode: {}'.format(mode))


    def test_change_read_permissions(self):
        with tempfile.NamedTemporaryFile() as fobj:
            # test change read permission to group target.
            fileope.change_read_permissions(path=fobj.name,
                                          target='g')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '040', msg="mode: {}".format(mode))
            # test change read permission to other target.
            fileope.change_read_permissions(path=fobj.name,
                                          target='o')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '004', msg="mode: {}".format(mode))
        del fobj

        with tempfile.NamedTemporaryFile() as fobj:
            # test change read permission to all target.
            fileope.change_read_permissions(path=fobj.name,
                                          target='a')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '444', msg='mode: {}'.format(mode))

    def test_change_exc_permissions(self):
        with tempfile.NamedTemporaryFile() as fobj:
            # test change exc permission to user target.
            fileope.change_exc_permissions(path=fobj.name,
                                          target='u')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '100', msg="mode: {}".format(mode))
            # test change exc permission to group target.
            fileope.change_exc_permissions(path=fobj.name,
                                          target='g')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '010', msg="mode: {}".format(mode))
            # test change exc permission to other target.
            fileope.change_exc_permissions(path=fobj.name,
                                        target='o')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '001', msg="mode: {}".format(mode))
        del fobj

        with tempfile.NamedTemporaryFile() as fobj:
            # test change write permission to all target.
            fileope.change_exc_permissions(path=fobj.name,
                                          target='a')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '111', msg='mode: {}'.format(mode))

    def test_change_permission(self):
        with tempfile.NamedTemporaryFile() as fobj:
            # change permission to 600 for test.
            fileope.change_permission(path=fobj.name,
                                      user_mode='6',
                                      grp_mode='0',
                                      oth_mode='0')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '600', msg='mode: {}'.format(mode))
            # change permission to 666 for test.
            fileope.change_permission(path=fobj.name,
                                      user_mode='6',
                                      grp_mode='6',
                                      oth_mode='6')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '666', msg='mode: {}'.format(mode))
            # change permission to 540 for test.
            fileope.change_permission(path=fobj.name,
                                      user_mode='5',
                                      grp_mode='4',
                                      oth_mode='0')
            mode = oct(os.stat(fobj.name).st_mode)[-3:]
            self.assertEqual(mode, '540', msg='mode: {}'.format(mode))


if __name__ == '__main__':
    unittest.main()