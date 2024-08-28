import subprocess
import requests
import sys
from langchain.tools import tool

@tool("verify_and_install_library", return_direct=True)
def verify_and_install_library(library_name: str) -> str:
    """
    This tool allows the agent to verify a Python library on PyPI and install it if it is safe.
    The function checks the library's existence, its release history, and whether it appears to be maintained.
    """
    pypi_url = f"https://pypi.org/pypi/{library_name}/json"
    response = requests.get(pypi_url)

    if response.status_code != 200:
        return f"Library '{library_name}' not found on PyPI."

    data = response.json()

    info = data.get('info', {})
    releases = data.get('releases', {})

    if not releases:
        return f"Library '{library_name}' has no releases on PyPI."

    latest_release = max(releases.keys(), default=None)
    if not latest_release:
        return f"Library '{library_name}' has no valid release versions."

    last_release_date = info.get('release_date', None)
    if last_release_date and last_release_date < '2022-01-01':
        return f"Library '{library_name}' has not been updated recently."

    maintainers = info.get('maintainers', [])
    if not maintainers:
        return f"Library '{library_name}' appears to have no maintainers."

    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", library_name])
        return f"Library '{library_name}' installed successfully."
    except subprocess.CalledProcessError as e:
        return f"Failed to install '{library_name}': {e}"

# Example usage if needed for testing
if __name__ == "__main__":
    print(verify_and_install_library("requests"))
