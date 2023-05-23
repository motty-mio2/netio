from dataclasses import dataclass, field
from ipaddress import ip_address


@dataclass
class host:
    rule_name: str
    ip_address: str
    external: bool = False


@dataclass
class configs:
    doamin: str
    hosts: list[host] = field(default_factory=list)
    inadyn: str = ""

    def export(self) -> None:
        pass
