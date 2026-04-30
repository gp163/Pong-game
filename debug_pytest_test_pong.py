import os
import sys

os.environ['SDL_VIDEODRIVER'] = 'windib'

with open('debug_pytest_test_pong.txt', 'w') as f:
    try:
        f.write('Starting pytest collect-only for test_pong.py\n')
        f.flush()
        import pytest
        f.write('Imported pytest\n')
        f.flush()
        exit_code = pytest.main(['--collect-only', '-q', 'test_pong.py'])
        f.write(f'pytest.main returned {exit_code}\n')
    except Exception as e:
        f.write(f'Exception: {e}\n')
        import traceback
        traceback.print_exc(file=f)
    finally:
        f.write('Done\n')
