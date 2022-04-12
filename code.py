# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import supervisor

from lib.circuitpy_mcu.mcu import Mcu


code = 'heating_relay.py'


supervisor.disable_autoreload()
supervisor.set_next_code_file(code, reload_on_success=False)
supervisor.reload()