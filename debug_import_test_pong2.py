import os
import sys
import importlib.util

os.environ['SDL_VIDEODRIVER'] = 'windib'

with open('debug_import_test_pong2.txt', 'w') as f:
    f.write('Starting debug import test_pong\n')
    f.flush()
    try:
        f.write('Importing pytest...\n')
        f.flush()
        import pytest
        f.write(f'pytest imported: {pytest.__version__}\n')
        f.flush()

        f.write('Importing pong_game...\n')
        f.flush()
        import pong_game
        f.write('pong_game imported\n')
        f.flush()

        f.write('Loading test_pong module with importlib...\n')
        f.flush()
        spec = importlib.util.spec_from_file_location('test_pong', 'test_pong.py')
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        f.write('test_pong module loaded\n')
    except Exception as e:
        f.write(f'Exception: {e}\n')
        import traceback
        traceback.print_exc(file=f)
    finally:
        f.write('Done\n')
