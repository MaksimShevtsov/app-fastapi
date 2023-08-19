"""Main.py"""
import logging
from logging.handlers import TimedRotatingFileHandler
from fastapi import FastAPI
from pydantic import BaseModel

from .settings import settings

class StatusPage(BaseModel):
    """Doc string"""
    message: str = "Hello, Fast api!"
    status: str = "success"


class Logger:
    """Doc string"""
    def __init__(self, logger_level=logging.INFO):
        self._logger = logging.getLogger()
        self._logger.setLevel(logger_level)

        self._formatter = logging.Formatter(
            '{asctime},{msecs:03.0f} {name} \
                | Level: {levelname} | Message: {message} \
              | FuncName: {funcName} | Line: {lineno} \
                | Thread: {thread} | Thread name: {threadName}',
            style='{'
        )
        self._handlers = []

    def _add_handler(self, handler):
        handler.setFormatter(self._formatter)
        handler.setLevel(self._logger.level)
        self._logger.addHandler(handler)
        self._handlers.append(handler)

    @property
    def console_handler(self):
        """This is doc string"""
        handler = logging.StreamHandler()
        self._add_handler(handler)
        return handler

    @property
    def file_handler(self):
        """This is doc string"""
        handler = TimedRotatingFileHandler('py_log.log', when='midnight', backupCount=7)
        self._add_handler(handler)
        return handler


# You can configure the log level here
LOGGER_LEVEL = logging.DEBUG  # Change this to your desired log level
logger = Logger(LOGGER_LEVEL)

app = FastAPI()


@app.on_event("startup")
async def startup_event():
    """Startup"""
    logger.console_handler
    logger.file_handler


@app.get(settings.home_url, response_model=StatusPage)
def read_first():
    """This is doc string"""
    logging.info("Request received for first endpoint")
    return StatusPage()
