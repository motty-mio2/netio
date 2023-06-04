import tomllib
from pathlib import Path
from typing import Any

from netio.config import c
from netio.model.base_host import host, parsed_data


def load(file: str | Path = "./sample.toml") -> parsed_data:
    with open(str(file)) as f:
        config: dict[str, Any] = tomllib.loads(f.read())

    c.set_export_dir(config["common"]["export"])

    domain = str(config["common"]["domain"])
    inadyn = str(config["inadyn"]["config"])

    hs = parsed_data(doamin=domain)
    hs.inadyn = inadyn

    for k, v in config["host"].items():
        h = host(
            rule_name=k,
            app_host_ip=v.get("app_host_ip", None),
            external=v.get("external", None),
            port=v.get("port", None),
        )
        hs.hosts.append(h)

    return hs
