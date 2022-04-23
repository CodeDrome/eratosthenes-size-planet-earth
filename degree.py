

class Degree(object):

    def __init__(self, degrees = 0, minutes = 0, seconds = 0):

        self._seconds = self._seconds_from_dms(degrees, minutes, seconds)


    def __str__(self):

        dms = self.get()

        return f"{dms['degrees']:02d}° {dms['minutes']:02d}′ {dms['seconds']:02d}″"


    def set(self, degrees = 0, minutes = 0, seconds = 0):

        self._seconds = _seconds_from_dms(degrees, minutes, seconds)


    def get(self):

        degrees = self._seconds // 3600
        minutes = (self._seconds - (degrees * 3600)) // 60
        seconds = self._seconds - (degrees * 3600) - (minutes * 60)

        return {"degrees": degrees, "minutes": minutes, "seconds": seconds}


    def _seconds_from_dms(self, degrees, minutes, seconds):

        return (degrees * 3600) + (minutes * 60) + (seconds)


    def fraction_of_circle(self):

        return self._seconds / 1_296_000


    def set_between(self, deg1, deg2):

        if deg1._seconds > deg2._seconds:
            self._seconds = deg1._seconds - deg2._seconds
        else:
            self._seconds = deg2._seconds - deg1._seconds


    def to_decimal(self):

        degrees = self._seconds // 3600
        remaining_seconds = (self._seconds - (degrees * 3600))
        decimal_fraction = remaining_seconds / 3600

        return degrees + decimal_fraction
