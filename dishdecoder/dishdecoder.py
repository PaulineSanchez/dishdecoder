"""Welcome to Pynecone! This file outlines the steps to create a basic app."""
from pcconfig import config

import pynecone as pc
from .helpers import navbar_index
from .helpers import navbar

docs_url = "https://pynecone.io/docs/getting-started/introduction"
filename = f"{config.app_name}/{config.app_name}.py"


class User(pc.Model, table=True):
    """A table for users in the database."""

    username: str
    password: str

class State(pc.State):
    """The app state."""
    
    username: str = ""
    password: str = ""

    def set_username(self, username):
        self.username = username.strip()

    def set_password(self, password):
        self.password = password.strip()

    def signup(self):
        with pc.session() as session:
            user = User(username=self.username, password=self.password)
            session.add(user)
            session.commit()
        self.logged_in = True
        return pc.redirect("/")


def index() -> pc.Component:
    return pc.center(
        navbar_index(),
        pc.vstack(
            pc.hstack(
            pc.heading("Dish Decoder", font_size="4em", font_family="BrunoAceSC"),
            pc.image(src="/logo.png", fit="heading"), spacing="1em"),
            pc.box("Get started by editing ", pc.code(filename, font_size="1em")),
            pc.button("Login", href="/login", color="primary"),
            pc.link(
                "Check out our docs!",
                href=docs_url,
                border="0.1em solid",
                padding="0.5em",
                border_radius="0.5em",
                _hover={
                    "color": "rgb(107,99,246)",
                },
            ),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="5%",
    )


def signup() -> pc.Component:
    return pc.center(
        navbar(),
        pc.vstack(
            pc.heading("Welcome to Dish Decoder !", font_size="2em"),
            pc.text("Sign up to get started", as_="em", font_size="1.5em"),
            pc.spacer(),
            pc.box(
            pc.hstack(
                pc.text("Username", as_="b"),
                pc.input(
                        on_blur=State.set_username, width="60%", placeholder="BestCookEver", justify="center"
                    ),
                    padding="0.5em", spacing="4.4em"
                    ),                        
            pc.hstack(
                pc.text("E-mail", as_="b"),
                pc.input(
                        on_blur=State.set_username, width="60%", placeholder="bestcookever@gmail.com"
                    ),
                    padding="0.5em", spacing="6.2em"
                    ),
            pc.hstack(
                pc.text("Password", as_="b"),
                pc.input(
                        type_="password", on_blur=State.set_password, width="60%", placeholder="Aa@Bb!90", justify="center"
                    ),
                    padding="0.5em", spacing="4.5em"
                    ),
            pc.hstack(
                pc.text("Confirm Password", as_="b"),
                pc.input(
                        type_="password", on_blur=State.set_password, width="60%", placeholder="Aa@Bb!90", justify="center"
                    ),
                    padding="0.5em"
                    ),
            pc.button("Sign Up", on_click=State.signup, width="100%"),
                ),
                shadow="lg",
                padding="1em",
                border_radius="lg",
                background="white",
                spacing="1em",
            ),
            padding_top="10%",
        )



# Add state and page to the app.
app = pc.App(state=State)
app.add_page(index, title="Dish Decoder")
app.add_page(signup)
app.compile()
