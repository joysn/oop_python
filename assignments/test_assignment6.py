import pytest
import os
from assignment6 import ConfigDict, ConfigKeyError
import shutil


class TestConfigDict:
    existing_fn = 'config_file.txt'
    existing_fn_template = 'config_file_template.txt'
    new_fn = 'config_file_new.txt'
    bad_path = '/a/b/doesnotexist.txt'

    def setup_class(self):
        shutil.copy(TestConfigDict.existing_fn_template, TestConfigDict.existing_fn)

    def teardown_class(self):
        os.remove(TestConfigDict.new_fn)

    def test_obj(self):
        cd = ConfigDict(TestConfigDict.existing_fn)
        assert isinstance(cd, ConfigDict)
        assert isinstance(cd, dict)

    def test_existing_fname(self):
        cd = ConfigDict(TestConfigDict.existing_fn)
        assert cd._fname == TestConfigDict.existing_fn

    def test_new_fname(self):
        assert not os.path.isfile(TestConfigDict.new_fn)
        cd = ConfigDict(TestConfigDict.new_fn)
        assert cd._fname == TestConfigDict.new_fn
        assert os.path.isfile(cd._fname)

    def test_bad_filepath(self):
        with pytest.raises(IOError):
            ConfigDict(TestConfigDict.bad_path)

    def test_read_dict(self):
        cd = ConfigDict(TestConfigDict.existing_fn)
        assert cd['a'] == '5'
        assert cd['b'] == '10'
        assert cd['c'] == 'this=that'

        with pytest.raises(ConfigKeyError):
            print(cd['x'])

    def test_write_dict(self):
        cd = ConfigDict(TestConfigDict.existing_fn)
        cd['zz'] = 'top'
        cd2 = ConfigDict(TestConfigDict.existing_fn)
        assert cd2['zz'] == 'top'
