import matplotlib

matplotlib.use("Agg")

from weather_forecast.plotter import plot_weather_data  # noqa: E402


def test_plot_weather_data_creates_png(chdir_tmp, sample_forecast_file):
    plot_weather_data(str(sample_forecast_file))

    png = chdir_tmp / "assets" / "forecast.png"
    assert png.exists()
    assert png.stat().st_size > 0
