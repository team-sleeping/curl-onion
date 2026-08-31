import subprocess
import shlex


class OnionCurl:
    def __init__(self, proxy="socks5h://127.0.0.1:9050"):
        self.proxy = proxy

    def run(self, curl_command):
        args = shlex.split(curl_command)

        if args[0] != "curl":
            raise ValueError("Command must start with curl")

        args = args[1:]

        if "--socks5-hostname" not in args and "--proxy" not in args:
            args = ["--proxy", self.proxy] + args

        result = subprocess.run(
            ["curl"] + args,
            capture_output=True,
            text=True
        )

        if result.returncode != 0:
            raise RuntimeError(result.stderr.strip())

        return result.stdout
