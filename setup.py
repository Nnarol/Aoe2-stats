from cx_Freeze import setup, Executable

# The scipy.spatial.cKDTree exclude is a workaround to a name-case conflict
# on Windows with a related file that prevents cx_Freeze from bundling the
# appropriate library.
buildOptions = dict(packages = ["matplotlib", "scipy", "pandas", "numpy", "requests", "seaborn"], namespace_packages = ["mpl_toolkits"], excludes = ["scipy.spatial.cKDTree"])

base = 'Console'

executables = [
    Executable('aoe2stats.py', base=base, targetName = 'aoe2stats')
]

setup(name='aoe2stats',
      version = '1.0',
      description = '',
      options = dict(build_exe = buildOptions),
      executables = executables)
