#!/bin/bash
MYDIR=$(dirname $0)
source "${MYDIR}/../setup.sh"

dropdb -U postgres hollywood_test
createdb -U postgres hollywood_test
psql -U postgres hollywood_test < "${MYDIR}/data.sql"

python3 "${MYDIR}/../test_app.py"