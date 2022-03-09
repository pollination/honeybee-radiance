from dataclasses import dataclass
from pollination_dsl.function import Function, command, Inputs, Outputs


@dataclass
class DCGlareGlareAutonomy(Function):
    """Calculates glare autonomy. The glare autonomy is the fraction of hours (occupied) 
    without any detected glare. The detection of glare is controlled by glare_limit."""

    dc_direct = Inputs.file(
        description='Path to dcdirect.', path='dc_direct.mtx',
    )

    dc_total = Inputs.file(
        description='Path to dctotal.', path='dc_total.mtx',
    )

    sky_vector = Inputs.file(
        description='Path to sky vector.', path='sky.smx'
    )

    view_rays = Inputs.file(
        description='Path to view ray.', path='view_rays.ray',
    )

    glare_limit = Inputs.float(
        description='Glare limit indicating presence of glare.', default=0.4
    )

    threshold_factor = Inputs.float(
        description='Constant threshold factor in cd/m2.', default=2000
    )

    occupancy_scheulde = Inputs.file(
        description='Path to occupancy schedule.', path='occupancy_schedule.csv',
    )

    @command
    def run_dcglare(self):
        return 'honeybee-radiance dcglare two-phase dc_direct.mtx dc_total.mtx ' \
            'sky.smx view_rays.ray --glare-limit {{self.glare_limit}} ' \
            '--threshold-factor "{{self.threshold_factor}}" --occupancy-schedule ' \
            '{{self.occupancy_schedule}} --output occupied.ga'

    dcglare_glare_autonomy = Outputs.file(
        description='Output dcglare glare autonomy file.', path='occupied.ga'
    )


@dataclass
class DCGlare(Function):
    """Calculates DGP for all sky conditions in the sky matrix."""

    dc_direct = Inputs.file(
        description='Path to dcdirect.', path='dc_direct.mtx',
    )

    dc_total = Inputs.file(
        description='Path to dctotal.', path='dc_total.mtx',
    )

    sky_vector = Inputs.file(
        description='Path to sky vector.', path='sky.smx'
    )

    view_rays = Inputs.file(
        description='Path to view ray.', path='view_rays.ray',
    )

    threshold_factor = Inputs.float(
        description='Constant threshold factor in cd/m2.', default=2000
    )

    @command
    def run_dcglare(self):
        return 'honeybee-radiance dcglare two-phase dc_direct.mtx dc_total.mtx ' \
            'sky.smx view_rays.ray --threshold-factor "{{self.threshold_factor}}" ' \
            '--output view_rays.dgp'

    view_rays_dgp = Outputs.file(
        description='Output dcglare dgp file.', path='view_rays.dgp'
    )


@dataclass
class DCGlareOccupancy(Function):
    """Calculates DGP for all sky conditions in the sky matrix, but filtered by an
    occupancy schedule. This means that unoccupied hours will be zero DGP."""

    dc_direct = Inputs.file(
        description='Path to dcdirect.', path='dc_direct.mtx',
    )

    dc_total = Inputs.file(
        description='Path to dctotal.', path='dc_total.mtx',
    )

    sky_vector = Inputs.file(
        description='Path to sky vector.', path='sky.smx'
    )

    view_rays = Inputs.file(
        description='Path to view ray.', path='view_rays.ray',
    )

    threshold_factor = Inputs.float(
        description='Constant threshold factor in cd/m2.', default=2000
    )

    occupancy_scheulde = Inputs.file(
        description='Path to occupancy schedule.', path='occupancy_schedule.csv',
    )

    @command
    def run_dcglare(self):
        return 'honeybee-radiance dcglare two-phase dc_direct.mtx dc_total.mtx ' \
            'sky.smx view_rays.ray --threshold-factor "{{self.threshold_factor}}" ' \
            '--occupancy-schedule {{self.occupancy_schedule}} --output occupied.dgp'

    occupied_dgp = Outputs.file(
        description='Output dcglare occupied dgp file.', path='occupied.dgp'
    )
