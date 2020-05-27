Generating a self-contained executable
--------------------------------------

1. Install cx-freeze.

   `pip install cx-freeze`

2. Generate the executable based on build configuration in setup.py.

   `python setup.py build_exe`

3. The build creates a new directory structure in the current directory for the output files.<br />The output is build/<platform_specific_directory>/aoe2stats.exe .

Usage
--------------------

When running the program, the lib directory created by the build, as well as the python DLL must be located where aoe2stats.exe is.<br />
aoe2stats.exe can be started like any regular program.
Since it is currently based on an experimental script, it does not have any parameters:

`aoe2stats.exe`
