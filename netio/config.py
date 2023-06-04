from dataclasses import dataclass
from pathlib import Path


@dataclass
class config:
    root_dir: Path = Path(__file__).parents[1]

    def set_export_dir(self, dir: str) -> None:
        if dir[0] == "~":
            self.export_dir: Path = Path(dir).expanduser()
        else:
            self.export_dir: Path = Path(dir).absolute()


c = config()
