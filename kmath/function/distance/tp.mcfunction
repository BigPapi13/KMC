
execute store result storage kmath:storage Pos[0] double 1 run scoreboard players get #d.x kmath
execute store result storage kmath:storage Pos[1] double 1 run scoreboard players get #d.y kmath
execute store result storage kmath:storage Pos[2] double 1 run scoreboard players get #d.z kmath
data modify entity @s Pos set from storage kmath:storage Pos

execute at @s facing 0.0 0.0 0.0 run tp @s 0 0 0 0 ~
execute store result storage kmath:macro distance_input int 1 run data get entity @s Rotation[1] 100
