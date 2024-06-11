class Band:
    def __init__(self, name, hometown):
        # This sets up the Band with its name and hometown
        self._name = name
        self._hometown = hometown
        # This will store all the concerts the band plays
        self._concerts = []

    @property
    def name(self):
        # This gets the band's name
        return self._name
    
    @name.setter
    def name(self, value):
        # This sets the band's name, but only if it's a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        # else:
        #    raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        # This gets the band's hometown
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        # This sets the band's hometown, but it can only be set once
        if self._hometown is not None:
            raise AttributeError("Hometown can't be changed once set")
        if isinstance(value, str) and len(value) > 0:
            self._hometown = value
        else:
            raise ValueError("Hometown must be a non-empty string")

    def concerts(self):
        # This returns the list of concerts the band has played
        return self._concerts

    def venues(self):
        # This returns a list of all the unique venues where the band has played
        return list({concert.venue for concert in self._concerts})

    def play_in_venue(self, venue, date):
        # This creates a new concert and adds it to the band's and venue's lists of concerts
        new_concert = Concert(date=date, band=self, venue=venue)
        # self._concerts.append(new_concert)
        # venue.add_concert(new_concert)
        return new_concert

    def all_introductions(self):
        # This returns a list of introduction phrases for all the band's concerts
        return [
            f"Hello {concert.venue.city}!!!!! We are {self.name} and we're from {self.hometown}"
            for concert in self._concerts
        ]

class Concert:
    # This keeps track of all concerts ever created
    all = []

    def __init__(self, date, band, venue):
        # This sets up the concert with a date, band, and venue
        self.date = date
        self.band = band
        self.venue = venue
        # Add this concert to the band's and venue's concert lists
        self.band._concerts.append(self)
        self.venue._concerts.append(self)
        # Add this concert to the global list of all concerts
        Concert.all.append(self)
        
    @property
    def date(self):
        # This gets the concert's date
        return self._date

    @date.setter
    def date(self, value):
        # This sets the concert's date, but only if it's a non-empty string
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        # This gets the concert's band
        return self._band

    @band.setter
    def band(self, value):
        # This sets the concert's band, but only if it's a Band object
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be of type Band")

    @property
    def venue(self):
        # This gets the concert's venue
        return self._venue

    @venue.setter
    def venue(self, value):
        # This sets the concert's venue, but only if it's a Venue object
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be of type Venue")

    def hometown_show(self):
        """Returns True if the concert is in the band's hometown, False otherwise."""
        return self.band.hometown == self.venue.city

    def introduction(self):
        """Returns a string with the band's introduction for this concert."""
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"

class Venue:
    def __init__(self, name, city):
        # This sets up the Venue with a name and city
        self.name = name
        self.city = city
        # This will store all the concerts at this venue
        self._concerts = []

    def concerts(self):
        """Returns the concerts associated with the venue."""
        return self._concerts

    def bands(self):
        """Returns the bands that have performed at the venue."""
        return list({concert.band for concert in self._concerts})

    def add_concert(self, concert):
        # Adds a concert to the venue's concert list
        self._concerts.append(concert)

    def concert_on(self, date):  # Added method
        """Returns the first concert on a specified date at the venue."""
        for concert in self._concerts:
            if concert.date == date:
                return concert
        return None
