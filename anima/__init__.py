from beet import Context
from beet.contrib.load import load

def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/anima/modules": "@kmc.anima/modules"
            },
        )
    )

    ctx.require("beet.contrib.model_merging")
