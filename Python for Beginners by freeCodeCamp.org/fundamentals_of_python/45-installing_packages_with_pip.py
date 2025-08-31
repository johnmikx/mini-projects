# pip --> Package Manager (for Python) or an acronym of 'pip Install Packages'
# PyPI --> Python Package Index, where are all collected in a single place 'pypi.org'
    # PyPI is the official third-party software repository for the Python programming language.

# --- First time ---
# python -m venv .venv
# .\.venv\Scripts\activate
# pip install jupyter numpy pandas scikit-learn matplotlib
# pip freeze > requirements.txt

# --- Every time ---
# .\.venv\Scripts\activate
# code .  # or just open VS Code

# In VS Code, select interpreter: Ctrl+Shift+P -> Python: Select Interpreter -> choose .venv

# --- When adding new packages ---
# pip install <package_name>
# pip freeze > requirements.txt

# --- When setting up from repo ---
# python -m venv .venv
# .\.venv\Scripts\activate
# pip install -r requirements.txt

# ---------------------------------------------------------------------
# Create a virtual environment named 'venv'
# python -m venv .venv

# Activate the virtual environment (Windows)
# .\.venv\Scripts\activate

# Upgrade pip (optional but recommended)
# python -m pip install --upgrade pip

# Install a package (replace [package_name] with the actual package)
# pip install [package_name]

# Upgrade certain package/s
# pip install -U [package_name]

# For requirements.txt folder (use it when project is done)
# pip freeze > requirements.txt

# To deactivate the virtual environment when done
# deactivate

# ---------------------------------------------------------------------
# OTHERS #

# Uninstalling package/s
# pip uninstall [package_name]

# Show information about certain package
# pip show [package_name]