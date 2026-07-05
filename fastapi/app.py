from fastapi import FastAPI
from fastapi.config import Env
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from fastapi.requests import Request
from fastapi.exceptions import HTTPException
from pydantic import BaseModel
from typing import List
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
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from jose import jwt, JWTError
from datetime import datetime, timedelta
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import Response
from fastapi import status
from fastapi.responses import JSONResponse
from fastapi import FastAPI
from fastapi import Request
from fastapi import Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import FastAPI, Form
from fastapi import FastAPI, File, UploadFile
from fastapi import FastAPI, BackgroundTasks
from fastapi import FastAPI, Depends
from fastapi import FastAPI, HTTPException
from fastapi import FastAPI, status
from fastapi import FastAPI, Response
from fastapi import FastAPI, Request
from fastapi import FastAPI, Response
from fastapi.responses import JSONResponse
from fastapi import FastAPI, Depends
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from fastapi import FastAPI, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from fastapi import FastAPI, Response
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
from fastapi import FastAPI, Response
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
app = FastAPI(
    title="Luca",
    description="A software used to train and create AI models with custom datasets.",
    version="1.0.0"
)
origins = [
    "*"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
