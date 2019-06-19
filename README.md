[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/hyperion-start/hyperion-ui/graphs/commit-activity)
[![GPLv3 license](https://img.shields.io/badge/License-GPLv3-blue.svg)](http://perso.crans.org/besson/LICENSE.html)

# Hyperion user interfaces extension

## What is Hyperion

Hyperion is an engine designed to launch and monitor user defined components using YAML configuration files.  
Inspired by [vdemo](https://code.cor-lab.org/projects/vdemo) and [TMuLE](https://github.com/marc-hanheide/TMuLE) (see [vdemo and TMuLE assessment](https://github.com/hyperion-start/hyperion-core/wiki/vdemo-and-TMuLE-assessment))

## How does it work
Hyperion (like TMuLE) is written in Python and utilizes the [tmux library for python](https://github.com/tmux-python/libtmux) to start components in detached sessions. For each host defined in the components a master session is created, in which each component will be started in a window. Components are managed by a main server that delegates commands to slave server instances on remote machines and forwards information to subscribed user interfaces.

## Installation

Run ```pip install . ``` in the main directory to install the ui extension. To start the PyQt gui, you also need to install python-qt4, since it is not automatically managed by pip.

## Quick reference

This library unlocks the ui mode for the hyperion application:

### UI mode (WORK IN PROGRESS)

```
usage: hyperion ui [-h] [-p PORT] [-H HOST | --no-socket] [-x]

optional arguments:
  -h, --help            show this help message and exit
  -p PORT, --port PORT  Specify port to connect to. Defaults to 23081
  -H HOST, --host HOST  Specify host to connect to. Defaults to localhost
  --no-socket           Start in standalone mode without connecting to a
                        running backend
  -x                    Use PyQt gui (requires X server and python-qt4
                        package)
```

UI mode starts a user interface (PyQt or interactive cli) which either connects to a running hyperion backend or if started in standalone mode runs its own backend. Note that the backend created by standalone mode will terminate when the ui is exited and unlike a backend started by server mode, it will not accept connections from other uis. 

Visit [Control GUI](https://github.com/hyperion-start/hyperion-core/wiki/Control-GUI) for detailed information about the GUI.  
Visit [Interactive CLI](https://github.com/hyperion-start/hyperion-core/wiki/Interactive-CLI-Mode) for detailed information about the interactive cli. 

