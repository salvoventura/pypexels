#!/usr/bin/env bash

# I cannot wait for the day Python 2 is finally nuked from orbit
# Anyway, flit doesn't work on Python 2, so build some rough
# approximation of our Python 3 builds
if hash python2 2>/dev/null; then
	sudo apt-get install jq
	cat Pipfile.lock | jq 'del(.develop.flit)' > Pipfile2.lock
	cat Pipfile | grep -v flit > Pipfile2
	mv Pipfile2 Pipfile
	mv Pipfile2.lock Pipfile.lock
fi
