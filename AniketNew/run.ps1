# Get the directory of the current script
$scriptDir = $PSScriptRoot

# Path to the virtual environment folder
$venvPath = Join-Path -Path $scriptDir -ChildPath "venv"

# Path to the Python executable inside the virtual environment
$pythonExe = Join-Path -Path $venvPath -ChildPath "Scripts\python.exe"

# Path to the main Python script
$pythonScript = Join-Path -Path $scriptDir -ChildPath "main.py"

# Execute the Python script using the Python executable from the virtual environment
& $pythonExe $pythonScript
