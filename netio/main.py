import argparse

from netio.model.base_host import parsed_data
from netio.model.formats.caddy import caddy
from netio.model.formats.coredns import coredns
from netio.model.formats.inadyn import inadyn
from netio.parser import load


def arg_parse() -> argparse.Namespace:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--input", type=str, default="sample.toml", help="input file name"
    )
    parser.add_argument("--output", type=str, default="export", help="output directory")

    return parser.parse_args()


def main() -> None:
    opt: argparse.Namespace = arg_parse()
    p: parsed_data = load(file=opt.input)

    coredns(parsed_data=p)
    caddy(parsed_data=p)
    inadyn(parsed_data=p)


if __name__ == "__main__":
    main()
