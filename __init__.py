from beet import Context
from beet.contrib.load import load
import yaml

def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/kmc/modules": "@kmc/modules",
            },
        )
    )
    ctx.require("bolt")
    ctx.require("bolt_expressions")


with open('kmc.yaml', 'r') as file:
    config = yaml.safe_load(file)