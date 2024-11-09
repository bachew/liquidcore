from . import sh
from attrs import define, field
from pathlib import Path
from typing_extensions import Self


@define
class Application:
    base_dir: Path = field(init=False)
    source_dirs: list[Path] = field(init=False)

    @base_dir.default
    def default_base_dir(self: Self):
        return Path(__file__).parents[2]

    @source_dirs.default
    def default_source_dirs(self: Self):
        return [
            self.base_dir / 'src',
            self.base_dir / 'tests',
        ]

    def lint(self: Self):
        for source_dir in self.source_dirs:
            sh.run(['flake8'], cwd=str(source_dir))

        for source_dir in self.source_dirs:
            sh.run(['mypy', '.'], cwd=str(source_dir))

    def do_something(self: Self):
        print('Doing something')
