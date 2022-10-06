#!/usr/bin/env bash

if [ "${WORK_DIR}" != "" ] ; then
    echo "Switching to directory '${WORK_DIR}'..."
    cd ${WORK_DIR}
fi

if [ "${PYTHON_SCRIPT}" != "" ] ; then
    echo "Running Python Script"
    python ${PYTHON_SCRIPT}
fi

git config --global user.name ${GH_USER_NAME}
git config --global user.email ${GH_USER_EMAIL}
git commit -am "Added new partitions"
git push