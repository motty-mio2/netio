from dataclasses import dataclass, field


@dataclass
class host:
    rule_name: str
    app_host_ip: str
    external: bool = False
    port: int = 80


@dataclass
class parsed_data:
    doamin: str
    hosts: list[host] = field(default_factory=list)

    coredns: str | None = None
    caddy: str | None = None
    inadyn: str | None = None

    def export(self) -> None:
        pass
