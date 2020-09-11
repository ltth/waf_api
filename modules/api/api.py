from fastapi import APIRouter
from modules.api.endpoints import add, delete, rollback, update, view, control

apiRouter = APIRouter()

apiRouter.include_router(view.route, prefix = "/view", tags = ["view"])
apiRouter.include_router(update.route, prefix = "/update", tags = ["update"])
apiRouter.include_router(add.route, prefix = "/add", tags = ["add"])
apiRouter.include_router(rollback.route, prefix = "/rollback", tags = ["rollback"])
apiRouter.include_router(delete.route, prefix = "/del", tags = ["delete"])
apiRouter.include_router(control.route, prefix = "/control", tags = ["control"])