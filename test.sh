#!/bin/bash

# create a package
pushd www/
zip -0 -r ../package.zip ./
popd

# run tests
source /home/zalun/Envs/marionette_venv/bin/activate
echo `python test.py`

# remove zip
#rm package.zip

