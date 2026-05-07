##README.md

# mypackage
mypackage is a python package

## Installation
```
pip install mypackage
```

## Usage
```
import mypackage
print(mypackage.hello())
```

# project package
python_package/
|--- mypackage/
|    |--- __init__.py
|    |--- mymodule.py
|    |--- message.py
|--- README.md
|--- setup.py
|--- pyproject.toml

# command
pip install .
pip list
pip show mypackage

# make wheel file
python -m build


## License
MIT License (MIT)

Copyright (c) 2017 Sanghee Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.