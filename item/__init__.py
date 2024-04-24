from beet import Context
from beet.contrib.load import load

print("ITEM LOADED")

def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/kmc.item/modules": "@kmc.item/modules",
            },
        )
    )

