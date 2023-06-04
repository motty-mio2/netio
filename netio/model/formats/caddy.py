from pathlib import Path
from netio.model.base_host import parsed_data
from netio.config import c


def caddy(parsed_data: parsed_data, directory: Path = c.root_dir, filename: str = "caddy") -> None:
    for h in parsed_data.hosts:
        dir: Path = Path()

        if h.external:
            dir = directory / "external"
            dir.mkdir(exist_ok=True)
        else:
            dir = directory / "internal"
            dir.mkdir(exist_ok=True)

        with open(dir / f"{h.rule_name}.{filename}", mode="w") as f:
            f.write((f"@{h.rule_name} host {h.rule_name}.{parsed_data.doamin}\n" f"handle @{h.rule_name} {'{'}\n"))
            if h.service_domain:
                f"\treverse_proxy {'{'} to {h.service_domain}:{h.port} {'}'}\n"
            f.write("}")
