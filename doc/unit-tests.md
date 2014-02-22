Compiling/running Marsmellod unit tests
------------------------------------

Marsmellod unit tests are in the `src/test/` directory; they
use the Boost::Test unit-testing framework.

To compile and run the tests:

	cd src
	make -f makefile.unix test_Marsmello  # Replace makefile.unix if you're not on unix
	./test_Marsmello   # Runs the unit tests

If all tests succeed the last line of output will be:
`*** No errors detected`

To add more tests, add `BOOST_AUTO_TEST_CASE` functions to the existing
.cpp files in the test/ directory or add new .cpp files that
implement new BOOST_AUTO_TEST_SUITE sections (the makefiles are
set up to add test/*.cpp to test_Marsmello automatically).


Compiling/running Marsmello-Qt unit tests
---------------------------------------

Marsmello-Qt unit tests are in the src/qt/test/ directory; they
use the Qt unit-testing framework.

To compile and run the tests:

	qmake Marsmello-qt.pro Marsmello_QT_TEST=1
	make
	./Marsmello-qt_test

To add more tests, add them to the `src/qt/test/` directory,
the `src/qt/test/test_main.cpp` file, and Marsmello-qt.pro.
