import sys
from cli import run_interactive, run_command_mode

if __name__ == "__main__":
    if len(sys.argv) > 1:
        run_command_mode()
    else:
        run_interactive()