
#### **sync.py**
```python
import shutil
import os

source = "/path/to/source"
destination = "/path/to/destination"

shutil.copytree(source, destination, dirs_exist_ok=True)
print(f"Files synchronized from {source} to {destination}")
