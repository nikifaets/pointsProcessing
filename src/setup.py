<<<<<<< HEAD
import sys
from cx_Freeze import Executable, setup

setup(

    name = "main",
    version = "0.1",
    executables = [Executable("main.py")]
)
=======
from cx_Freeze import setup, Executable
import sys

setup(
	name = "main",
	version = "0.1",
	executables = [Executable("main.exe")]
	)
>>>>>>> master
