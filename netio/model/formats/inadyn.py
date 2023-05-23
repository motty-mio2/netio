from netio.model.base_host import configs, host


def inadyn(configs: configs, filename: str = "inadyn.conf") -> None:
    with open(filename, mode="w") as f:
        f.write("provider cloudflare.com {\n")
        f.write(f"    {configs.inadyn}\n")
        f.write("    hostname = { \n")
        for host in configs.hosts:
            if host.external:
                f.write(f"    {host.rule_name}.{configs.doamin},\n")

        f.write("    }\n")
        f.write("}")
