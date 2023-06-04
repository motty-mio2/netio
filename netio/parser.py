from pathlib import Path
import tomllib
from typing import Any

from netio.model.base_host import parsed_data, host
from netio.model.formats.caddy import caddy
from netio.model.formats.coredns import coredns
from netio.model.formats.inadyn import inadyn


def load(file: str | Path = "./sample.toml") -> parsed_data:
    with open(str(file)) as f:
        config: dict[str, Any] = tomllib.loads(f.read())

    print(config)

    domain = str(config["common"]["domain"])
    inadyn = str(config["inadyn"]["config"])

    hs = parsed_data(doamin=domain)
    hs.inadyn = inadyn

    for k, v in config["host"].items():
        h = host(
            rule_name=k,
            ip_address=v.get("ip_address", None),
            external=v.get("external", None),
            port=v.get("port", None),
            service_domain=v.get("service_domain", None),
        )
        hs.hosts.append(h)

    return hs


p: parsed_data = load()

coredns(parsed_data=p)
caddy(parsed_data=p)
inadyn(parsed_data=p)
