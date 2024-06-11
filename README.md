# Band and Concert Management System

## Overview

This project provides a simple system to manage bands, their concerts, and the venues where they perform. It consists of three main classes: `Band`, `Concert`, and `Venue`. These classes allow you to create bands, schedule concerts, and manage venue information.

## Classes and Their Responsibilities

### Band Class

The `Band` class represents a musical band. It contains information about the band's name, hometown, and the concerts they have performed.

#### Attributes

- `name` (str): The name of the band. This attribute can be changed.
- `hometown` (str): The hometown of the band. This attribute is immutable once set.
- `_concerts` (list): A list of concerts the band has performed.

#### Methods

- `name` (property): Getter and setter for the band's name.
- `hometown` (property): Getter and setter for the band's hometown.
- `concerts()`: Returns a list of concerts the band has performed.
- `venues()`: Returns a list of venues where the band has performed.
- `play_in_venue(venue, date)`: Schedules a new concert for the band at the specified venue and date.
- `all_introductions()`: Returns a list of introductions for each concert.

### Concert Class

The `Concert` class represents a concert performed by a band at a venue on a specific date.

#### Attributes

- `date` (str): The date of the concert.
- `band` (Band): The band performing at the concert.
- `venue` (Venue): The venue where the concert is held.
- `all` (list): A class attribute that keeps track of all concerts.

#### Methods

- `date` (property): Getter and setter for the concert date.
- `band` (property): Getter and setter for the band performing.
- `venue` (property): Getter and setter for the venue of the concert.
- `hometown_show()`: Returns `True` if the concert is in the band's hometown, `False` otherwise.
- `introduction()`: Returns a string with the band's introduction for the concert.

### Venue Class

The `Venue` class represents a venue where concerts can be held.

#### Attributes

- `name` (str): The name of the venue.
- `city` (str): The city where the venue is located.
- `_concerts` (list): A list of concerts held at the venue.

#### Methods

- `concerts()`: Returns a list of concerts associated with the venue.
- `bands()`: Returns a list of bands that have performed at the venue.
- `add_concert(concert)`: Adds a concert to the venue's list of concerts.
- `concert_on(date)`: Returns the first concert on a specified date at the venue.

## Usage

### Creating a Band

```python
band = Band(name="The Rockers", hometown="Rockville")
