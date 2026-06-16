import os

try:
    import requests
except ImportError:
    requests = None


class FileManager:
    @staticmethod
    def scan_directory(directory, extension=".txt"):
        return [f for f in os.listdir(directory) if f.endswith(extension)]

    @staticmethod
    def download_image(url, output_dir):
        if requests is None:
            print("Warning: requests is not installed; image download skipped.")
            return None

        try:
            response = requests.get(url, stream=True)
            if response.status_code == 200:
                file_name = os.path.join(output_dir, os.path.basename(url))
                with open(file_name, "wb") as f:
                    for chunk in response.iter_content(1024):
                        f.write(chunk)
                return file_name
            else:
                print(f"Failed to download image: {url}")
        except Exception as e:
            print(f"Error downloading image: {e}")
        return None
