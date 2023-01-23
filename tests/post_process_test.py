import os

from ladybug.futil import nukedir
from pollination.honeybee_radiance.post_process import ConvertToBinary, SumRow, \
    AnnualIrradianceMetrics, AnnualDaylightMetrics, LeedIlluminanceCredits, \
    SolarTrackingSynthesis, DaylightFactorConfig, DaylightFactorVisMetadata, \
    ImagelessAnnualGlareVisMetadata

from queenbee.plugin.function import Function


def test_convert_to_binary():
    function = ConvertToBinary().queenbee
    assert function.name == 'convert-to-binary'
    assert isinstance(function, Function)


def test_sum_row():
    function = SumRow().queenbee
    assert function.name == 'sum-row'
    assert isinstance(function, Function)


def test_annual_irradiance_metrics():
    function = AnnualIrradianceMetrics().queenbee
    assert function.name == 'annual-irradiance-metrics'
    assert isinstance(function, Function)


def test_annual_daylight_metrics():
    function = AnnualDaylightMetrics().queenbee
    assert function.name == 'annual-daylight-metrics'
    assert isinstance(function, Function)


def test_leed_illuminance_credits():
    function = LeedIlluminanceCredits().queenbee
    assert function.name == 'leed-illuminance-credits'
    assert isinstance(function, Function)


def test_solar_tracking_synthesis():
    function = SolarTrackingSynthesis().queenbee
    assert function.name == 'solar-tracking-synthesis'
    assert isinstance(function, Function)


def test_daylight_factor_config():
    function = DaylightFactorConfig().queenbee
    assert function.name == 'daylight-factor-config'
    assert isinstance(function, Function)


def test_daylight_factor_vis_metadata():
    function = DaylightFactorVisMetadata()
    qb_function = function.queenbee
    assert qb_function.name == 'daylight-factor-vis-metadata'
    assert isinstance(qb_function, Function)

    inputs = {} # inputs is empty for this function
    folder = './tests/assets/temp'
    output_file = os.path.join(folder, 'vis_metadata.json')
    function._try(inputs, folder=folder)
    assert os.path.isfile(output_file)

    nukedir(folder)


def test_imageless_annual_glare_vis_metadata():
    function = ImagelessAnnualGlareVisMetadata()
    qb_function = function.queenbee
    assert qb_function.name == 'imageless-annual-glare-vis-metadata'
    assert isinstance(qb_function, Function)

    inputs = {} # inputs is empty for this function
    folder = './tests/assets/temp'
    output_file = os.path.join(folder, 'vis_metadata.json')
    function._try(inputs, folder=folder)
    assert os.path.isfile(output_file)

    nukedir(folder)
