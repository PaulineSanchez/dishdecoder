import pynecone as pc

config = pc.Config(
    app_name="dishdecoder",
    db_url="sqlite:///pynecone.db",
    env=pc.Env.DEV,
    frontend_packages=[
        "react-image-crop", "croppr"
    ],
)
