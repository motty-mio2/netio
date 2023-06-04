from pathlib import Path
from netio.model.base_host import parsed_data
from netio.config import c


def coredns(parsed_data: parsed_data, directory: Path = c.root_dir, filename: str = "mio2") -> None:
    with open(directory / filename, mode="w") as f:
        for h in parsed_data.hosts:
            f.write(f"{h.ip_address} {h.rule_name}.{parsed_data.doamin}\n")
