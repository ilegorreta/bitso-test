#!/usr/bin/env bash

if [ "${WORK_DIR}" != "" ] ; then
    echo "Switching to directory '${WORK_DIR}'..."
    cd ${WORK_DIR}
fi

if [ "${PYTHON_SCRIPT}" != "" ] ; then
    echo "Running Python Script"
    python ${PYTHON_SCRIPT}
fi
