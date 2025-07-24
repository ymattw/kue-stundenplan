import base64
import pytz
from icalendar import Calendar, Event, Timezone, TimezoneStandard, TimezoneDaylight
from datetime import datetime, timedelta


# Weekdays mapping (Monday=0, Sunday=6)
WEEKDAYS = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
}

START_TIMES = [
    "07:25",
    "08:15",
    "09:10",
    "10:15",
    "11:10",
    "12:00",
    "12:50",
    "13:40",
    "14:35",
    "15:30",
    "16:20",
    "17:05",
]


class ICAL:

    def __init__(self, name, start_date, end_date, *, tzid="Europe/Zurich"):
        self.start_date = start_date
        self.end_date = end_date
        self.tzid = tzid
        self.cal = Calendar()
        self.cal.add("X-WR-CALNAME", name)
        self.cal.add("UID", base64.b64encode(name.encode("utf-8")))
        self.cal.add("VERSION", "2.0")
        self.cal.add("PRODID", "-//KUE//Stundenplan//EN")

    def add_timezone_component(self):
        self._add_component(self._create_timezone_component())

    # Deprecated
    def add_event(self, weekday, timestr, title, duration_minutes=45):
        day_offset = WEEKDAYS[weekday]
        start_time = datetime.strptime(timestr, "%H:%M").time()
        event = Event()
        event.add("summary", title)

        # Calculate the actual date for the event
        event_start = datetime.combine(
            self.start_date + timedelta(days=day_offset), start_time
        )
        event_end = event_start + timedelta(minutes=duration_minutes)

        # Set the time
        event.add("dtstart", event_start, parameters={"TZID": self.tzid})
        event.add("dtend", event_end, parameters={"TZID": self.tzid})

        # Set the recurrence rule (weekly)
        event.add("rrule", {"freq": "weekly", "until": self.end_date})

        self.cal.add_component(event)

    def add_events(self, weekday, event_titles):
        day_offset = WEEKDAYS[weekday]
        for i in range(len(event_titles)):
            title = event_titles[i]
            if not title:
                continue

            event = Event()
            event.add("summary", title)

            # Calculate the actual date for the event
            start_time = datetime.strptime(START_TIMES[i], "%H:%M").time()
            event_start = datetime.combine(
                self.start_date + timedelta(days=day_offset), start_time
            )
            event_end = event_start + timedelta(minutes=45)

            # Set the time
            event.add("dtstart", event_start, parameters={"TZID": self.tzid})
            event.add("dtend", event_end, parameters={"TZID": self.tzid})

            # Set the recurrence rule (weekly)
            event.add("rrule", {"freq": "weekly", "until": self.end_date})

            self.cal.add_component(event)

    def write_file(self, output_file):
        with open(output_file, "wb") as f:
            f.write(self.cal.to_ical())

    def _add_component(self, component):
        self.cal.add_component(component)

    def _create_timezone_component(self):
        """
        Create an iCalendar Timezone component with automatic DST transitions.

        Parameters:
            tzid (str): Timezone identifier (e.g., 'Europe/Zurich').
            start_date (datetime): Start of the range.
            end_date (datetime): End of the range.

        Returns:
            Timezone: An iCalendar Timezone component.
        """
        # Find DST transitions in the given range
        transitions = self._find_dst_transitions()
        timezone = Timezone()
        timezone.add("TZID", self.tzid)

        # Add each transition as a component
        for transition_date, old_offset, new_offset in transitions:
            # Determine if it's a DST start or end
            is_dst = new_offset > old_offset
            component = TimezoneDaylight() if is_dst else TimezoneStandard()

            # Add transition details
            transition_aware = pytz.timezone(self.tzid).localize(
                transition_date, is_dst=None
            )
            component.add("DTSTART", transition_aware)
            component.add("TZNAME", transition_aware.tzname())
            component.add("TZOFFSETFROM", old_offset)
            component.add("TZOFFSETTO", new_offset)

            # Add component to the timezone
            timezone.add_component(component)

        return timezone

    def _find_dst_transitions(self):
        """
        Find daylight saving transitions in the given period.

        Parameters:
            start_date (datetime): Start of the range.
            end_date (datetime): End of the range.
            tzid (str): Timezone identifier (e.g., 'Europe/Zurich').

        Returns:
            list: list of tuples with the transition datetime & offset changes.
        """
        tzinfo = pytz.timezone(self.tzid)
        transitions = []

        # Initialize variables for comparison
        current_date = self.start_date
        previous_offset = tzinfo.utcoffset(current_date)

        # Iterate hour by hour for fine granularity
        while current_date <= self.end_date:
            try:
                # Localize the date and resolve DST conflicts
                aware_date = tzinfo.localize(current_date, is_dst=None)
                current_offset = aware_date.utcoffset()

                # Check if the offset has changed
                if current_offset != previous_offset:
                    transitions.append(
                        (current_date, previous_offset, current_offset)
                    )
                    previous_offset = current_offset

            except pytz.NonExistentTimeError:
                # Skip invalid times due to DST transition
                pass
            except pytz.AmbiguousTimeError:
                # Handle ambiguous times during transitions (clocks go back)
                pass

            # Increment the date by 1 hour
            current_date += timedelta(hours=1)

        return transitions
