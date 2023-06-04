import socket

from netio.config import c
from netio.model.base_host import parsed_data

ip = socket.gethostbyname(socket.gethostname())


def coredns(parsed_data: parsed_data, filename: str = "mio2") -> None:
    with open(c.export_dir / f"core.{filename}", mode="w") as f:
        for h in parsed_data.hosts:
            f.write(f"{ip} {h.rule_name}.{parsed_data.doamin}\n")

        f.write(f"\n{parsed_data.coredns}")
