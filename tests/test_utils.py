import numpy as np
from PIL import Image
import pytest
from utils import download_utils as du
from utils import video_io

def test_save_videos_from_pil_gif(tmp_path):
    frames = [
        Image.fromarray(np.zeros((2, 2, 3), dtype=np.uint8)),
        Image.fromarray(np.ones((2, 2, 3), dtype=np.uint8) * 127),
        Image.fromarray(np.ones((2, 2, 3), dtype=np.uint8) * 255),
    ]
    out = tmp_path / "out.gif"
    video_io.save_videos_from_pil(frames, str(out), fps=5)
    assert out.exists()

def test_download_utils_calls_snapshot(monkeypatch, tmp_path):
    fake_file = tmp_path / "pkg" / "download_utils.py"
    fake_file.parent.mkdir(parents=True, exist_ok=True)
    fake_file.write_text("x")
    monkeypatch.setattr(du, "__file__", str(fake_file))

    calls = []
    monkeypatch.setattr(du, "snapshot_download", lambda **kwargs: calls.append(kwargs))
    monkeypatch.setattr(du, "hf_hub_download", lambda *a, **k: None)

    du.download_files_from_repo()
    assert len(calls) == 2
