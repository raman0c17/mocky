"""Filesystem helpers: scan input directories and download referenced images."""

from __future__ import annotations

import os
from urllib.parse import urlparse

try:
    import requests
except ImportError:
    requests = None

# Only fetch images over http(s); reject anything else.
_ALLOWED_SCHEMES = {"http", "https"}
_DOWNLOAD_TIMEOUT = 15  # seconds


class FileManager:
    @staticmethod
    def scan_directory(directory, extension=".txt"):
        """Return the files in ``directory`` ending with ``extension``."""
        if not os.path.isdir(directory):
            return []
        return [f for f in os.listdir(directory) if f.endswith(extension)]

    @staticmethod
    def download_image(url, output_dir):
        """Download ``url`` into ``output_dir`` and return the local path.

        Returns ``None`` if the download is skipped or fails. Only http(s)
        URLs are fetched, with a timeout, since Markdown input is untrusted.
        """
        if requests is None:
            print("Warning: requests is not installed; image download skipped.")
            return None

        parsed = urlparse(url)
        if parsed.scheme not in _ALLOWED_SCHEMES:
            print(f"Skipping non-http(s) image URL: {url}")
            return None

        try:
            response = requests.get(url, stream=True, timeout=_DOWNLOAD_TIMEOUT)
            if response.status_code == 200:
                os.makedirs(output_dir, exist_ok=True)
                file_name = os.path.join(output_dir, os.path.basename(parsed.path))
                with open(file_name, "wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                return file_name
            print(f"Failed to download image ({response.status_code}): {url}")
        except Exception as e:  # noqa: BLE001
            print(f"Error downloading image: {e}")
        return None
