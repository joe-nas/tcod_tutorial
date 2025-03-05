import tcod

from actions import EscapeAction, MovementAction
from input_handlers import EventHandler
from entity.entity import Entity


def main() -> None:
    screen_width = 80
    screen_height = 50

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    # comes from import input_handlers
    event_handler = EventHandler()

    # initialize entity objects:
    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

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
            root_console.print(
                x=player.x, y=player.y, string=player.char, fg=player.color
            )

            context.present(root_console)

            # given we are not creating a snake clone, we need to clear the console before we draw sth else
            root_console.clear()

            # events are handled by a queue managed by SDL2(Simple DirectMedia Layer)
            for event in tcod.event.wait():

                action = event_handler.dispatch(event=event)

                if action is None:
                    continue

                if isinstance(action, MovementAction):
                    player.move(dx=action.dx, dy=action.dy)

                elif isinstance(action, EscapeAction):
                    raise SystemExit()


if __name__ == "__main__":
    main()
