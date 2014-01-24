#!/usr/bin/env bash

function basedir()
{
    local script_path=`realpath "${BASH_SOURCE[0]}"`
    pushd . > /dev/null
    cd `dirname ${script_path}` > /dev/null
    script_path=`pwd`
    popd > /dev/null
    if [[ $script_path =~ Pmw$ ]]; then
        script_path=`dirname ${script_path}`
    fi
    echo $script_path
}

echo `basedir`
