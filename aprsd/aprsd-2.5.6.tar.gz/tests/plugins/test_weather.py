from unittest import mock

from aprsd.plugins import weather as weather_plugin

from .. import fake, test_plugin


class TestUSWeatherPluginPlugin(test_plugin.TestPlugin):

    @mock.patch("aprsd.config.Config.check_option")
    def test_not_enabled_missing_aprs_fi_key(self, mock_check):
        # When the aprs.fi api key isn't set, then
        # the LocationPlugin will be disabled.
        mock_check.side_effect = Exception
        wx = weather_plugin.USWeatherPlugin(self.config)
        expected = "USWeatherPlugin isn't enabled"
        packet = fake.fake_packet(message="weather")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_aprs_fi")
    def test_failed_aprs_fi_location(self, mock_check):
        # When the aprs.fi api key isn't set, then
        # the Plugin will be disabled.
        mock_check.side_effect = Exception
        wx = weather_plugin.USWeatherPlugin(self.config)
        expected = "Failed to fetch aprs.fi location"
        packet = fake.fake_packet(message="weather")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_aprs_fi")
    def test_failed_aprs_fi_location_no_entries(self, mock_check):
        # When the aprs.fi api key isn't set, then
        # the Plugin will be disabled.
        mock_check.return_value = {"entries": []}
        wx = weather_plugin.USWeatherPlugin(self.config)
        expected = "Failed to fetch aprs.fi location"
        packet = fake.fake_packet(message="weather")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_aprs_fi")
    @mock.patch("aprsd.plugin_utils.get_weather_gov_for_gps")
    def test_unknown_gps(self, mock_weather, mock_check_aprs):
        # When the aprs.fi api key isn't set, then
        # the LocationPlugin will be disabled.
        mock_check_aprs.return_value = {
            "entries": [
                {
                    "lat": 10,
                    "lng": 11,
                    "lasttime": 10,
                },
            ],
        }
        mock_weather.side_effect = Exception
        wx = weather_plugin.USWeatherPlugin(self.config)
        expected = "Unable to get weather"
        packet = fake.fake_packet(message="weather")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_aprs_fi")
    @mock.patch("aprsd.plugin_utils.get_weather_gov_for_gps")
    def test_working(self, mock_weather, mock_check_aprs):
        # When the aprs.fi api key isn't set, then
        # the LocationPlugin will be disabled.
        mock_check_aprs.return_value = {
            "entries": [
                {
                    "lat": 10,
                    "lng": 11,
                    "lasttime": 10,
                },
            ],
        }
        mock_weather.return_value = {
            "currentobservation": {"Temp": "400"},
            "data": {
                "temperature": ["10", "11"],
                "weather": ["test", "another"],
            },
            "time": {"startPeriodName": ["ignored", "sometime"]},
        }
        wx = weather_plugin.USWeatherPlugin(self.config)
        expected = "400F(10F/11F) test. sometime, another."
        packet = fake.fake_packet(message="weather")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)


class TestUSMetarPlugin(test_plugin.TestPlugin):

    @mock.patch("aprsd.config.Config.check_option")
    def test_not_enabled_missing_aprs_fi_key(self, mock_check):
        # When the aprs.fi api key isn't set, then
        # the LocationPlugin will be disabled.
        mock_check.side_effect = Exception
        wx = weather_plugin.USMetarPlugin(self.config)
        expected = "USMetarPlugin isn't enabled"
        packet = fake.fake_packet(message="metar")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_aprs_fi")
    def test_failed_aprs_fi_location(self, mock_check):
        # When the aprs.fi api key isn't set, then
        # the Plugin will be disabled.
        mock_check.side_effect = Exception
        wx = weather_plugin.USMetarPlugin(self.config)
        expected = "Failed to fetch aprs.fi location"
        packet = fake.fake_packet(message="metar")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_aprs_fi")
    def test_failed_aprs_fi_location_no_entries(self, mock_check):
        # When the aprs.fi api key isn't set, then
        # the Plugin will be disabled.
        mock_check.return_value = {"entries": []}
        wx = weather_plugin.USMetarPlugin(self.config)
        expected = "Failed to fetch aprs.fi location"
        packet = fake.fake_packet(message="metar")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_weather_gov_metar")
    def test_gov_metar_fetch_fails(self, mock_metar):
        mock_metar.side_effect = Exception
        wx = weather_plugin.USMetarPlugin(self.config)
        expected = "Unable to find station METAR"
        packet = fake.fake_packet(message="metar KPAO")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_weather_gov_metar")
    def test_airport_works(self, mock_metar):

        class Response:
            text = '{"properties": {"rawMessage": "BOGUSMETAR"}}'
        mock_metar.return_value = Response()

        wx = weather_plugin.USMetarPlugin(self.config)
        expected = "BOGUSMETAR"
        packet = fake.fake_packet(message="metar KPAO")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)

    @mock.patch("aprsd.plugin_utils.get_weather_gov_metar")
    @mock.patch("aprsd.plugin_utils.get_aprs_fi")
    @mock.patch("aprsd.plugin_utils.get_weather_gov_for_gps")
    def test_metar_works(self, mock_wx_for_gps, mock_check_aprs, mock_metar):
        mock_wx_for_gps.return_value = {
            "location": {"metar": "BOGUSMETAR"},
        }

        class Response:
            text = '{"properties": {"rawMessage": "BOGUSMETAR"}}'

        mock_check_aprs.return_value = {
            "entries": [
                {
                    "lat": 10,
                    "lng": 11,
                    "lasttime": 10,
                },
            ],
        }
        mock_metar.return_value = Response()

        wx = weather_plugin.USMetarPlugin(self.config)
        expected = "BOGUSMETAR"
        packet = fake.fake_packet(message="metar")
        actual = wx.filter(packet)
        self.assertEqual(expected, actual)
