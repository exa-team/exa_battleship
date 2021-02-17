import os
import sys

import uvicorn

sys.path.append(os.getcwd())


if __name__ == "__main__":
    from server import app

    uvicorn.run(app=app, port=5000)
