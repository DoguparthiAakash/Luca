from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from typing import List, Optional
import uvicorn
import os
import sys
import json
from fastapi import File, UploadFile
from fastapi.staticfiles import StaticFiles
from fastapi import BackgroundTasks
from fastapi import status
from fastapi import HTTPException
from fastapi import Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Response
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI, BackgroundTasks
from fastapi import FastAPI, Depends
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, status
from fastapi import FastAPI, Response
from fastapi import FastAPI, Request
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Response
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI, BackgroundTasks
from fastapi import FastAPI, Depends
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, status
from fastapi import FastAPI, Response
from fastapi import FastAPI, Request
from fastapi import Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
class Services:
    def __init__(self, app: FastAPI):
        self.app = app
    def get_items(self):
        return [
            {
                "name": "Item 1",
                "description": "This is item 1.",
                "price": 10.99,
                "tax": 1.99
            },
            {
                "name": "Item 2",
                "description": "This is item 2.",
                "price": 9.99,
                "tax": 1.49
            }
        ]
