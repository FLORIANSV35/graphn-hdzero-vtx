import logging

import serial
import serial.tools.list_ports

from external.send import do_send

Import("env")

SDCC_OPTS = ["--model-large", "--opt-code-speed", "--peep-return",
             "--fomit-frame-pointer", "--allow-unsafe-read"]

env.Append(
    CFLAGS=SDCC_OPTS,
    LINKFLAGS=SDCC_OPTS
)

def upload_firmware(source, target, env):
    ports = list(serial.tools.list_ports.grep("USB"))

    if len(ports) == 0:
        raise Exception("No serial port found, exiting")

    firmware = env.subst("$BUILD_DIR/HDZERO_TX.bin")
    do_send(ports[0].device, firmware)
                
env.Replace(UPLOADCMD=upload_firmware)


def graphn_version():
    """YY.MM.NN like the goggle firmware: year, month, and the number of commits since the 1st of the
    month (so NN rolls over by itself at the start of each month). None when git is not available."""
    import datetime
    import subprocess
    try:
        now = datetime.date.today()
        out = subprocess.check_output(
            ["git", "log", "--since=%04d-%02d-01 00:00" % (now.year, now.month), "--oneline"],
            cwd=env.subst("$PROJECT_DIR"), stderr=subprocess.DEVNULL).decode()
        return now.year % 100, now.month, len([l for l in out.splitlines() if l.strip()])
    except Exception:
        return None


_version = graphn_version()
if _version and _version[2] > 0:
    env.Append(CPPDEFINES=[
        ("VTX_VERSION_MAJOR", _version[0]),
        ("VTX_VERSION_MINOR", _version[1]),
        ("VTX_VERSION_PATCH_LEVEL", _version[2]),
        ("VTX_VERSION_STRING", env.StringifyMacro("%02d.%02d.%02d" % _version)),
    ])
    print("graphn VTX version %02d.%02d.%02d" % _version)
