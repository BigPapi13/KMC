from beet import Context
from beet.contrib.load import load

def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/kmc.ui/modules": "@kmc.ui/modules",
            },
            resource_pack={
                "assets/kmc.ui/textures": "@kmc.ui/textures",
                "assets/kmc.ui/models": "@kmc.ui/models"
            }
        )
    )


