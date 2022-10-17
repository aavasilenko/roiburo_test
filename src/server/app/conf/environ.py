"""Read .env file"""

import os.path

import environ  # type: ignore

ENV_PATH = "app/env/env"
EXAMPLE_TEST_PATH = "app/env/env.sample"

env = environ.Env()

if os.path.exists(ENV_PATH):
    environ.Env.read_env(ENV_PATH)
else:
    environ.Env.read_env(EXAMPLE_TEST_PATH)

__all__ = [
    "env",
]
