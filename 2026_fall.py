#!/usr/bin/env python3

from datetime import datetime

from ical import ICAL

name = "KUE Stundenplan (Herbstsemester 2026)"
output_file = "2026_fall.ics"


def main():
    start_date = datetime(2026, 8, 17)
    end_date = datetime(2027, 2, 14)
    cal = ICAL(name=name, start_date=start_date, end_date=end_date)
    cal.add_timezone_component()

    cal.add_events(
        "Monday",
        [
            "",
            "",
            "BP2 / Inf1",
            "BP2 / Inf1",
            "F / Gyg",
            "",
            "G / Haa",
            "G / Haa",
            "E / Zha",
            "E / Zha",
            "Robml / vb2 /",
            "Robml / /",
        ],
    )

    cal.add_events(
        "Tuesday",
        [
            "BP1 / Inf2",
            "BP1 / Inf2",
            "M / Lou",
            "M / Lou",
            "Sm / Hof",
            "Sw / Bul",
            "",
            "AM / Sal",
            "BG / Mu",
            "BG / Mu",
        ],
    )

    cal.add_events(
        "Wednesday",
        [
            "",
            "G / Haa",
            "Gg / Sty",
            "KI / Lou,Ebe",
            "AM / Sal",
            "",
            "",
            "D / Wam",
            "D / Wam",
        ],
    )

    cal.add_events(
        "Thursday",
        [
            "",
            "",
            "F / Gyg",
            "F / Gyg",
            "E / Zha",
            "ftr / tast",
            "ba2 / awe / tanz2",
            "",
            "",
            "",
            "vb1 / tanz1",
        ],
    )

    cal.add_events(
        "Friday",
        [
            "Gg1 / sty",
            "Gg2 / sty",
            "M / Lou",
            "D1 / M2",
            "D2 / M1",
            "",
            "fb1 / scha",
            "D / Wam",
            "AM / Sal",
            "Sm,Sw / Bul,Hof",
        ],
    )

    cal.write_file(output_file)
    print(f"Calendar wrote to {output_file} successfully")


if __name__ == "__main__":
    main()
