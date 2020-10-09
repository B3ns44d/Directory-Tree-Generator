# Generating Pretty Directory Tree Visualisation

![](<https://img.shields.io/badge/python3-passing-brightgreen.svg>)
![](<https://img.shields.io/badge/Video%20record-support-brightgreen.svg>)
![](<https://img.shields.io/badge/Sound-support-brightgreen.svg>)
![](<https://img.shields.io/badge/Sparse%20data-support-brightgreen.svg>)
![](<https://img.shields.io/badge/Resampling%20data-support-brightgreen.svg>)


## Introduction
A Directory Tree Generator lets me visualize the relationship between files and directories, thereby making it easier to understand the positioning of files and directories. For this project, I use os library to list the files and directories within a specific directory.

- Output

````
B3ns44d@zt:~/Documents/python-project/Directory_Tree_Gen$ python script.py 
Directory_Tree_Gen
|-- README.md
|-- script.py
'-- .git
    |-- config
    |-- HEAD
    |-- description
    |-- objects
    |   |-- info
    |   '-- pack
    |-- info
    |   '-- exclude
    |-- hooks
    |   |-- pre-push.sample
    |   |-- post-update.sample
    |   |-- pre-commit.sample
    |   |-- commit-msg.sample
    |   |-- pre-receive.sample
    |   |-- fsmonitor-watchman.sample
    |   |-- update.sample
    |   |-- applypatch-msg.sample
    |   |-- pre-applypatch.sample
    |   |-- pre-merge-commit.sample
    |   |-- pre-rebase.sample
    |   '-- prepare-commit-msg.sample
    |-- branches
    '-- refs
        |-- tags
        '-- heads
````
