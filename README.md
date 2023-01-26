# TestAndPractice
For testing and validating and practicing


# Logging

tip1: 
The call to basicConfig() should come before any calls to debug(), info(), etc. Otherwise, those functions will call basicConfig() for you with the default options. As it’s intended as a one-off simple configuration facility, only the first call will actually do anything: subsequent calls are effectively no-ops.