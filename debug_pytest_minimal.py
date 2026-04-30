import os
import sys

os.environ['SDL_VIDEODRIVER'] = 'windib'
with open('debug_pytest_minimal.txt', 'w') as f:
    try:
        f.write('Starting minimal test\n')
        f.flush()
        import pytest
        f.write('Imported pytest\n')
        f.flush()
        exit_code = pytest.main(['-q', 'test_minimal.py'])
        f.write(f'Exit code: {exit_code}\n')
    except Exception as e:
        f.write('Exception: ' + str(e) + '\n')
        import traceback
        traceback.print_exc(file=f)
    finally:
        f.write('Done\n')
