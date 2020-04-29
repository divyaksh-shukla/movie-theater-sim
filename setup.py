from cx_Freeze import setup, Executable

# Dependencies are automatically detected, but it might need
# fine tuning.
buildOptions = dict(packages = [], excludes = [])

import sys
base = 'Win32GUI' if sys.platform=='win32' else None

executables = [
    Executable('ttk_gui.py', base=base, targetName = 'movie_theater_sim')
]

setup(name='Movie Theater Simulator',
      version = '0.1',
      description = 'A simple simulation program',
      options = dict(build_exe = buildOptions),
      executables = executables)
