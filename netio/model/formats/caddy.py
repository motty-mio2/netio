from netio.model.base_host import configs, host


def caddy(configs: configs, filename: str = "caddy") -> None:
    with open(f"{host.rule_name}.{filename}", mode="w") as f:
        for host in configs.hosts:
            f.write(f"{host.ip_address} {host.rule_name}.{configs.doamin}\n")
