import oop_python29
import pytest
import os
from shutil import copy


class TestDoubleit(object):
    numbers_file_template = 'testnums_template.txt'
    numbers_file_testor = 'testnums.txt'

    def setup_class(self):
        copy(TestDoubleit.numbers_file_template, TestDoubleit.numbers_file_testor)

    def teardown_class(self):
        os.remove(TestDoubleit.numbers_file_testor)

    def test_doublelines(self):
        myprogram.doublelines(TestDoubleit.numbers_file_testor)
        old_vals = [int(line) for line in open(TestDoubleit.numbers_file_template)]
        new_vals = [int(line) for line in open(TestDoubleit.numbers_file_testor)]
        for old_val, new_val in zip(old_vals, new_vals):
            assert int(new_val) == int(old_val) * 2

    def test_doubleit(self):
        assert myprogram.doubleit(10) == 20

    def test_doubleit_type(self):
        with pytest.raises(TypeError):
            myprogram.doubleit('hello')



