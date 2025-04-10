# -*- coding: utf-8 -*-
import pytest
from theheck.rules.ln_no_hard_link import match, get_new_command
from theheck.types import Command

error = "hard link not allowed for directory"


@pytest.mark.parametrize('script, output', [
    ("ln barDir barLink", "ln: ‘barDir’: {}"),
    ("sudo ln a b", "ln: ‘a’: {}"),
    ("sudo ln -nbi a b", "ln: ‘a’: {}")])
def test_match(script, output):
    command = Command(script, output.format(error))
    assert match(command)


@pytest.mark.parametrize('script, output', [
    ('', ''),
    ("ln a b", "... hard link"),
    ("sudo ln a b", "... hard link"),
    ("a b", error)])
def test_not_match(script, output):
    command = Command(script, output)
    assert not match(command)


@pytest.mark.parametrize('script, result', [
    ("ln barDir barLink", "ln -s barDir barLink"),
    ("sudo ln barDir barLink", "sudo ln -s barDir barLink"),
    ("sudo ln -nbi a b", "sudo ln -s -nbi a b"),
    ("ln -nbi a b && ls", "ln -s -nbi a b && ls"),
    ("ln a ln", "ln -s a ln"),
    ("sudo ln a ln", "sudo ln -s a ln")])
def test_get_new_command(script, result):
    command = Command(script, '')
    assert get_new_command(command) == result
