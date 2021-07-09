---
name: Bug report
about: Create a report to help us improve
title: ''
labels: ''
assignees: ''

---
**Before opening a new issue**
Install the **staging** branch and check if the unexpected behavior is happening there as well.
You have to clone the repository and install it with pip:
```
git clone https://github.com/iontelos/waffles.git -b staging --depth=1
cd waffles
python3 -m venv venv
venv/bin/pip install pip --upgrade
venv/bin/pip install setuptools --upgrade
venv/bin/pip install -r requirements.txt
venv/bin/pip install .
venv/bin/waffles  # or venv/bin/waffles-tray
```
 
**Describe the bug**
A clear and concise description of what the bug is.

**Software Environment**
bauh version: 
O.S: name and version 
Python version:
Installation method: pip | distro package manager (e.g: pacman)


P.S: these instructions and the template must be respected, otherwise your issue will be closed.
