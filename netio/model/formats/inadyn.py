from pathlib import Path
from netio.model.base_host import parsed_data
from netio.config import c


def inadyn(parsed_data: parsed_data, directory: Path = c.root_dir, filename: str = "inadyn.conf") -> None:
    with open(directory / filename, mode="w") as f:
        f.write("provider cloudflare.com {\n")
        f.write(f"    {parsed_data.inadyn}\n")
        f.write("    hostname = { \n")
        for h in parsed_data.hosts:
            if h.external:
                f.write(f"    {h.rule_name}.{parsed_data.doamin},\n")

        f.write("    }\n")
        f.write("}")
