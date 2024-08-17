from beet import Context
from beet.contrib.load import load

def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/kmath/modules": "@kmc.kmath/modules",
                "data/kmath/function": "@kmc.kmath/function"
            },
        )
    )

    ctx.require("bolt_expressions")
