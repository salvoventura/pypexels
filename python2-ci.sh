#!/usr/bin/env bash

# I cannot wait for the day Python 2 is finally nuked from orbit
# Anyway, flit doesn't work on Python 2, so build some rough
# approximation of our Python 3 builds
if hash python2 2>/dev/null; then
	cat Pipfile | grep -v flit > Pipfile2
	mv Pipfile2 Pipfile
fi
