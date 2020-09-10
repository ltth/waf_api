'''
import os, sys
dirModule = os.path.abspath(os.path.join('modules'))
sys.path.append(dirModule)
'''

from modules.api import api
from fastapi import FastAPI

app = FastAPI()

app.include_router(api.apiRouter, prefix = "/api")