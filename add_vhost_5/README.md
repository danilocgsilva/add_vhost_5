# Objects and its roles (remember the Single Responsability principle)

## File_Checker

Utility to general file checking. Have methods as `exists`, to check if file exists and `is_writable`. Uses the `set_file` to *set a file* to be checked.

## File_Guesser

*Guess* some **file paths** (think the file path as its main responsability, as other file aspects have others *owners*) related to the virtual host configuration. Its responsability is guess the path from the *hosts file* and *virtual host* configuration file. Have the `set_os` so can split the hosts based on the operational system. The value provided in this method must be `platform` from `sys` (`from sys import platform`), and only 'linux', 'darwin' or 'win32' should be received. It implements the `File_Guesser_Interface`, so will obey mandatory methods realted to its responsability, that is guess the hosts file and the virtual host file configuration (`guess_host_file` and `guess_vhosts_configuration_path`, respectively).
Also have the `set_root` method, designed to be used only in the unit tests, so can exists a test to check if the file exists before returns value.

## File_Guesser_Interface

The interface to be implemented by the `File_Guesser` and force mandatory method. Initially planned to be implemented by a *file guesser* that could be based on the operational system, but just one file guesser is enouth tio do the task.

## File_Writter

General and generic file utility. Can easity writes in the file and check if file is writable. Useful to be used to write in the hosts file and the virtual host file configuration.

## Os_Definition_Exception

Custom exception to enlarge control over flow problems.

## VHost_Contents

Responsability to deal with contents both from hosts file and the virtual host configuration file. Think that the file content is something different from the paths.
