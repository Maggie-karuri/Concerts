class Band:
    def __init__(self, name, hometown):
        
        self._name = name
        self._hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
       # else:
        #    raise ValueError("Name must be a non-empty string")


    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if self._hometown is not None:
            raise AttributeError("Hometown is immutable and cannot be changed")
        if isinstance(value, str) and len(value) > 0:
            self._hometown = value
        else:
            raise ValueError("Hometown must be a non-empty string")

    def concerts(self):
        return self._concerts

    def venues(self):
        return list({concert.venue for concert in self._concerts})

    def play_in_venue(self, venue, date):
        new_concert = Concert(date=date, band=self, venue=venue)
        #self._concerts.append(new_concert)
        #venue.add_concert(new_concert)
        return new_concert

    def all_introductions(self):
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self._concerts
        ]

class Concert:
    all = []

    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        self.band._concerts.append(self)
        self.venue._concerts.append(self)
        Concert.all.append(self)
        
    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be of type Band")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be of type Venue")

    def hometown_show(self):
        """Returns True if concert is in band's hometown, False otherwise."""
        return self.band.hometown == self.venue.city

    def introduction(self):
        """Returns a string with the band's introduction for this concert."""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    def concerts(self):
        """Returns the concerts associated with the venue."""
        return self._concerts

    def bands(self):
        """Returns the bands that have performed at the venue."""
        return list({concert.band for concert in self._concerts})

    def add_concert(self, concert):
        self._concerts.append(concert)
    def concert_on(self, date):  # Added method
        """Returns the first concert on a specified date at the venue."""
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
