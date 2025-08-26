import yaml
from pathlib import Path

def test_default_config_loads(tmp_path):
    """YAML config should load without errors."""
    sample_config = tmp_path / "config.yaml"
    sample_config.write_text("""
    model:
      name: test-model
      layers: 2
    training:
      epochs: 1
      batch_size: 4
    """)
    with open(sample_config) as f:
        cfg = yaml.safe_load(f)
    assert "model" in cfg
    assert cfg["training"]["epochs"] == 1
