from netio.config import c
from netio.model.base_host import parsed_data


def inadyn(parsed_data: parsed_data, filename: str = "inadyn.conf") -> None:
    with open(c.export_dir / filename, mode="w") as f:
        f.write("provider cloudflare.com {\n")
        f.write(f"{parsed_data.inadyn}\n")
        f.write("\thostname = { \n")
        for h in parsed_data.hosts:
            if h.external:
                f.write(f"\t\t{h.rule_name}.{parsed_data.doamin},\n")

        f.write("\t}\n")
        f.write("}")
