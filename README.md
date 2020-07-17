# python-test-architecture
Examples of possible architectures to use when working with testing in python 

## Testing with Tox
After cloning the repository tox can be utilized to run the test suit. Tox is set up to utilize the test runner stestr and python 3.8. **To do this tox and stestr need to be installed in your environment!**

To run tox navigate to the root directory of the repo. From there run tox by entering `tox` into the terminal. The result should look as follows.

    python-test-architecture git:(master) ✗ tox
    GLOB sdist-make: /<path>/python-test-architecture/setup.py
    py38 create: /<path>/python-test-architecture/.tox/py38
    py38 installdeps: -r/<path>/python-test-architecture/requirements.txt
    py38 inst: /<path>/python-test-architecture/.tox/.tmp/package/1/Main_Module-0.1.dev0.zip
    py38 installed: attrs==19.3.0,cliff==3.3.0,cmd2==1.2.1,colorama==0.4.3,extras==1.0.0,fixtures==3.0.0,future==0.18.2,linecache2==1.0.0,Main-Module @ file:///<path>/python-test-architecture/.tox/.tmp/package/1/Main_Module-0.1.dev0.zip,pbr==5.4.5,prettytable==0.7.2,pyparsing==2.4.7,pyperclip==1.8.0,python-mimeparse==1.6.0,python-subunit==1.4.0,PyYAML==5.3.1,six==1.15.0,stestr==3.0.1,stevedore==3.1.0,testtools==2.4.0,traceback2==1.4.0,unittest2==1.1.0,voluptuous==0.11.7,wcwidth==0.2.5
    py38 run-test-pre: PYTHONHASHSEED='273657815'
    py38 run-test: commands[0] | stestr run
    {0} main_module.test.test_zero.TestZero.test_zero [0.000080s] ... ok
    {1} main_module.submodule2.test.test_two.TestZero.test_zero [0.000083s] ... ok
    {2} main_module.submodule1.test.test_one.TestZero.test_zero [0.000157s] ... ok
    
    ======
    Totals
    ======
    Ran: 3 tests in 0.0038 sec.
     - Passed: 3
     - Skipped: 0
     - Expected Fail: 0
     - Unexpected Success: 0
     - Failed: 0
    Sum of execute time for each test: 0.0003 sec.
    
    ==============
    Worker Balance
    ==============
     - Worker 0 (1 tests) => 0:00:00.000080
     - Worker 1 (1 tests) => 0:00:00.000083
     - Worker 2 (1 tests) => 0:00:00.000157
    ________________________________________________________________________________ summary ________________________________________________________________________________
      py38: commands succeeded
      congratulations :)


## Instalation 
Navigate to the root directory of the repo. From there run

	pip install .
to install the module, alternatively 

	pip install -e .
to install the module in an editable mode.

## Post-installation testing

The main point for using this architecture is the possibility to run tests after the module is installed and to be able to trigger the testing from inside python. The test runner is stestr, just as when running using tox, so the testing is completely equivalent. This way of testing also allows for highly selective testing and testing of submodules independently.

To run the complete test suite run 

	python -c 'import main_module; main_module.test()'
and to run the tests for just a submodule run 

	python -c 'import main_module.submodule1; main_module.submodule1.test()'

The output will be similar to that of the test initiated via tox.

No new functionality is needed to be implemented in a module or submodule, which is a huge plus. This is done by letting every new model register a unit tester which takes care of the stestr initiation.

## Uninstalling
To uninstall the module after the testing is done run

	pip uninstall main_module

This will not remove the logfiles stestr creates. Those have to be removed manually.

The logfiles could be configured to be placed elsewhere or not placed at all, but as it is configured now they are placed in the root of the module (or submodule) they are testing.
