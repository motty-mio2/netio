from netio.model.base_host import configs, host


def coredns(configs: configs, filename: str = "mio2") -> None:
    with open(filename, mode="w") as f:
        for host in configs.hosts:
            f.write(f"{host.ip_address} {host.rule_name}.{configs.doamin}\n")
