from pathlib import Path
import tomllib
from typing import Any

from netio.model.base_host import configs, host
from netio.model.formats.coredns import coredns
from netio.model.formats.inadyn import inadyn


def load(file: str | Path = "./sample.toml") -> configs:
    with open(str(file)) as f:
        config: dict[str, Any] = tomllib.loads(f.read())

    print(config)

    domain = str(config["common"]["domain"])
    inadyn = config["inadyn"]["config"]

    hs = configs(doamin=domain)
    hs.inadyn = inadyn

    for k, v in config["host"].items():
        h = host(rule_name=k, ip_address=v["ip_address"], external=v["external"])
        hs.hosts.append(h)

    return hs


p: configs = load()

coredns(configs=p)
inadyn(configs=p)
