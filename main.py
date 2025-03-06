import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
from entity.entity import Entity
from engine.engine import Engine

# from game_map import GameMap

from proc_gen import generate_dungeon


def main() -> None:
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # comes from import input_handlers
    event_handler = EventHandler()

    # initialize entity objects:
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    # initialize game_map
    # game_map = GameMap(map_width, map_height)
    game_map = generate_dungeon(map_width, map_height)

    # initialize our game Engine:
    engine = Engine(
        entities=entities, event_handler=event_handler, game_map=game_map, player=player
    )

    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="YART",
        vsync=True,
    ) as context:
        root_console = tcod.console.Console(
            screen_width, screen_height, order="F"
        )  ## order="F" sets numpy 2d array order to be [x,y] instead of [y,x]
        while True:
            engine.render(console=root_console, context=context)

            # blocks until event occurs. returns an iterator
            events = tcod.event.wait()

            engine.handle_events(events)


if __name__ == "__main__":
    main()
