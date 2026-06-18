from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class EPWtoDaylightHours(Function):
    """Convert EPW to EN 17037 schedule as a CSV file.
    
    This function generates a valid schedule for EN 17037, also known as daylight hours.
    Rather than a typical occupancy schedule, the daylight hours is half the year with
    the largest quantity of daylight.
    """

    epw = Inputs.file(
        description='Path to epw or wea file.', path='weather.epw', extensions=['epw', 'wea']
    )

    @command
    def create_daylight_hours(self):
        return 'honeybee-radiance schedule epw-to-daylight-hours weather.epw ' \
            '--name daylight_hours'

    daylight_hours_csv = Outputs.file(
        description='Path to daylight hours schedule as CSV.', path='daylight_hours.csv'
    )

    daylight_hours_json = Outputs.file(
        description='Path to daylight hours schedule as DataCollection.', path='daylight_hours.json'
    )

    daylight_hours_wea = Outputs.file(
        description='Path to converted Wea file.', path='daylight_hours.wea'
    )
