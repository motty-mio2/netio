from pathlib import Path

from netio.config import c
from netio.model.base_host import parsed_data


def caddy(parsed_data: parsed_data, filename: str = "caddy") -> None:
    for h in parsed_data.hosts:
        dir: Path = Path()

        if h.external:
            dir = c.export_dir / "external"
            dir.mkdir(exist_ok=True)
        else:
            dir = c.export_dir / "internal"
            dir.mkdir(exist_ok=True)

        with open(dir / f"{h.rule_name}.{filename}", mode="w") as f:
            f.write(
                (
                    f"@{h.rule_name} host {h.rule_name}.{parsed_data.doamin}\n"
                    f"handle @{h.rule_name} {'{'}\n"
                )
            )
            f.write(
                f"\treverse_proxy {'{'}\n\t\tto {h.app_host_ip}:{h.port}\n\t{'}'}\n"
            )
            f.write("}")
