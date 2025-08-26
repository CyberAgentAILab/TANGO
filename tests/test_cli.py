import importlib.util
import subprocess
import sys
import pytest

# Skip the whole module if "tango" is not importable
spec = importlib.util.find_spec("tango")
pytestmark = pytest.mark.skipif(spec is None, reason="tango package not importable")

def test_cli_help_runs():
    """CLI --help should exit cleanly and show usage message."""
    result = subprocess.run(
        [sys.executable, "-m", "tango", "--help"],
        capture_output=True,
        text=True
    )
    assert result.returncode == 0
    out = (result.stdout or "").lower()
    err = (result.stderr or "").lower()
    assert "usage" in out or "usage" in err or "--help" in out
