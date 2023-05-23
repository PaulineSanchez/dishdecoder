import pynecone as pc


def navbar_index():
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.text("Decode Recipes, Translate Tastes - Dish Decoder!", as_="em"),
                pc.image(src="/magic-wand.png", width="30px"),
            ),
            pc.hstack(
                pc.link(pc.button("Sign up", bg="RGB(30, 130, 76)", color="white", border_radius="md", px=4, py=2), href="/signup", width="100%"),
                pc.link(pc.button("Login", bg="RGB(30, 130, 76)", color="white", border_radius="md", px=4, py=2),
                        ),
            ),
            justify="space-between",
            padding_x="2em",
            padding_y="1em",
            bg="RGB(249, 180, 45)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )

def navbar():
    return pc.box(
        pc.hstack(
            pc.hstack(
                pc.text("Decode Recipes, Translate Tastes - Dish Decoder!", as_="em"),
                pc.image(src="/magic-wand.png", width="30px"),
            ),
            pc.text("Dish Decoder", as_="b", align="center", font_size="2em"),
            pc.link(pc.button("Return", bg="RGB(30, 130, 76)", color="white", border_radius="md", px=4, py=2), href="/", width="100%"),   
            
            justify="space-between",
            padding_x="2em",
            padding_y="1em",
            bg="RGB(249, 180, 45)",
        ),
        position="fixed",
        width="100%",
        top="0px",
        z_index="500",
    )