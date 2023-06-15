import pynecone as pc

class DishdecoderConfig(pc.Config):
    pass

config = DishdecoderConfig(
    app_name="dishdecoder",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
)