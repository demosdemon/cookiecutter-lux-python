{{ cookiecutter.shebang_python }}
{{ cookiecutter.shebang_coding }}

import pytest

from {{ cookiecutter.repo_name }} import *
from {{ cookiecutter.repo_name }}.tests.test_{{ cookiecutter.repo_name }} import *


class Test{{ cookiecutter.class_name }}:

    def _setup(self) -> None:
        pass

    def _teardown(self) -> None:
        pass

    def test_{{ cookiecutter.repo_name }}(self) -> None:
        self._setup()
        assert True
        self._teardown()


if __name__ == '__main__':
    pytest.main(args=[__file__])
