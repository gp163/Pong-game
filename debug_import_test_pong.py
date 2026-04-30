import os
import sys

os.environ['SDL_VIDEODRIVER'] = 'windib'

with open('debug_import_test_pong.txt', 'w') as f:
    f.write('Starting import test_pong\n')
    f.flush()
    try:
        import test_pong
        f.write('Imported test_pong successfully\n')
    except Exception as e:
        f.write('Import exception: ' + str(e) + '\n')
        import traceback
        traceback.print_exc(file=f)
    finally:
        f.write('Done\n')
