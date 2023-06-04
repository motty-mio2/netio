from dataclasses import dataclass
from pathlib import Path


@dataclass
class config:
    root_dir: Path = Path(__file__).parents[1]

    def __post_init__(self) -> None:
        self.root_dir = self.root_dir / "export"

        self.root_dir.mkdir(exist_ok=True)


c = config()
