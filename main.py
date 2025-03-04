import tcod


def main() -> None:
    screen_width = 80
    screen_height = 50

    player_x = int(screen_width / 2)
    player_y = int(screen_height / 2)

    tileset = tcod.tileset.load_tilesheet(
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    with tcod.context.new(
        columns=screen_width,
        rows=screen_height,
        tileset=tileset,
        title="YART",
        vsync=True,
    ) as context:
        root_console = tcod.Console(
            screen_width, screen_height, order="F"
        )  ## order="F" sets numpy 2d array order to be [x,y] instead of [y,x]
        while True:
            root_console.print(x=player_x, y=player_y, string="@")

            context.present(root_console)

            for event in tcod.event.wait():
                if event.type == "QUIT":
                    raise SystemExit


if __name__ == "__main__":
    main()
