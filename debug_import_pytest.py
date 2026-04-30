import os
import sys
with open('debug_import_pytest.txt', 'w') as f:
    try:
        f.write('Starting import pytest\n')
        f.flush()
        import pytest
        f.write('Import success: ' + pytest.__version__ + '\n')
    except Exception as e:
        f.write('Import exception: ' + str(e) + '\n')
        import traceback
        traceback.print_exc(file=f)
    finally:
        f.write('Done\n')
