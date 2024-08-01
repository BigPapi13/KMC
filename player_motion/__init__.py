from beet import Context
from beet.contrib.load import load


def beet_default(ctx: Context):
    ctx.require(
        load(
            data_pack={
                "data/player_motion/modules": "@kmc.player_motion/modules",
                "data/player_motion/function": "@kmc.player_motion/player_motion/function",
                "data/minecraft/tags": "@kmc.player_motion/minecraft/tags"
            },
        )
    )

    ctx.require("kmc.kmath")
