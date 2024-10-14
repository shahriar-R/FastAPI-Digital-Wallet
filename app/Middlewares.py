import logging
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware

logging.basicConfig(level=logging.INFO)

class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        
        logging.info(f"Request: {request.method} {request.url}")

        response = await call_next(request)

        logging.info(f"Response: {response.status_code}")

        return response
