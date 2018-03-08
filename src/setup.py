from cx_Freeze import setup, Executable
import sys

setup(
	name = "main",
	version = "0.1",
	executables = [Executable("main.py")]
	)
