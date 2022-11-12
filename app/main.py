import subprocess

from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import PlainTextResponse

app = FastAPI()


def run_subprocess(command):
    return subprocess.Popen(command, shell=True, stdout=subprocess.PIPE).stdout.read()


class ShellCommand(BaseModel):
    command: str


@app.post("/command/", response_class=PlainTextResponse)
async def run_command(shell_command: ShellCommand):
    return run_subprocess(shell_command.command)
