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
    return pc.vstack( 
        pc.center(
        navbar_index(),
        pc.vstack(
            pc.hstack(
            pc.heading("Dish Decoder", font_size="4em", font_family="BrunoAceSC"),
            pc.image(src="/logo.png", fit="heading"), spacing="1em"),
            spacing="1.5em",
            font_size="2em",
        ),
        padding_top="7%",),
        pc.spacer(),
            pc.hstack(
                pc.box(
                    pc.tabs(
                        items=[
                            ("English", pc.list(items=["Welcome to Dish Decoder!", "Dish Decoder is an application where you can perform OCR on a recipe and translate it.", "Not sure what it means ?", "Just try it!"], font_size="2em", spacing=".25em")),
                            ("Français", pc.list(items=["Bienvenue sur Dish Decoder !", "Dish Decoder est une application où vous pouvez effectuer de l'OCR sur une recette et la traduire.", "Vous ne savez pas ce que cela signifie ?", "Essayez-le tout simplement!"], font_size="2em", spacing=".25em")),
                        ],
                        bg="RGB(244, 237, 228)",
                        color="black",
                        shadow="lg",
                        position="left",
                        width="75%",
                        padding_x="1em",
                        font_family="BrunoAceSC",
                    ),
                    #padding_x="25em",
                    padding_y="5em",
                    width="80%",
                    ),
                pc.button(
                        "TRY IT NOW",
                        border_radius="1em",
                        size="lg",
                        box_shadow="rgba(151, 65, 252, 0.8) 0 15px 30px -10px",
                        background_image="linear-gradient(144deg,#AF40FF,#5B42F3 50%,#00DDEB)",
                        box_sizing="border-box",
                        color="white",
                        _hover={
                            "opacity": 0.85,
                        },
                        padding_x="5em"
                ), 
            width="80%"),
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
