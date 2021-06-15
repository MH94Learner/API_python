from darksky.api import DarkSky
from darksky.types import languages, units, weather


#API_KEY = 'private key...'

darksky = DarkSky(API_KEY)

latitude = 51.5074
longitude = -0.1278
forecast = darksky.get_forecast(
    latitude, longitude,
    extend=False, # default `False`
    lang=languages.ENGLISH, # default `ENGLISH`
    values_units=units.AUTO, # default `auto`
    exclude=[weather.MINUTELY, weather.ALERTS] # default `[]`
)

print(forecast.currently.temperature)

forecast.latitude 
forecast.longitude 
forecast.timezone # timezone for coordinates. For exmaple: `America/New_York`

forecast.currently # CurrentlyForecast. 
forecast.minutely # MinutelyForecast. 
forecast.hourly # HourlyForecast. 
forecast.daily # DailyForecast. 
forecast.alerts # [Alert]. 