"""
GCode M115
Get Firmware Version and Capabilities

Author: Mathieu Monney
email: zittix(at)xwaves(dot)net
Website: http://www.xwaves.net
License: CC BY-SA: http://creativecommons.org/licenses/by-sa/2.0/
"""

from GCodeCommand import GCodeCommand

class M115(GCodeCommand):
    def execute(self, g):
        protocol_version = 0.1
        replicape_key = self.printer.replicape_key
        firmware_name = "Redeem"
        firmware_version = self.printer.firmware_version
        firmware_url = "http%3A//wiki.thing-printer.com/index.php?title=Redeem"
        machine_type = self.printer.config.get('System', 'machine_type')
        extruder_count = self.printer.NUM_AXES - 3
        g.set_answer(
            "ok " \
            "PROTOCOL_VERSION:{} "\
            "FIRMWARE_NAME:{} "\
            "FIRMWARE_VERSION:{} "\
            "REPLICAPE_KEY:{} "\
            "FIRMWARE_URL:{} "\
            "MACHINE_TYPE:{} "\
            "EXTRUDER_COUNT: {}".format(
                protocol_version,
                firmware_name,
                firmware_version,
                replicape_key,
                firmware_url,
                machine_type,
                extruder_count
            )
        )

    def get_description(self):
        return "Get Firmware Version and Capabilities"

    def get_long_description(self):
        return ("Get Firmware Version and Capabilities"
                "Will return the version of Redeem running, "
                "the machine type and the extruder count. ")
