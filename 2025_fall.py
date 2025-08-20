#!/usr/bin/env python3

from datetime import datetime

from ical import ICAL

name = "KUE Stundenplan (Herbstsemester 2025)"
output_file = "2025_fall.ics"


def main():
    start_date = datetime(2025, 8, 18)
    end_date = datetime(2026, 2, 21)
    cal = ICAL(name=name, start_date=start_date, end_date=end_date)
    cal.add_timezone_component()

    cal.add_events(
        "Monday",
        [
            "BG2 / A215 / Kue",
            "BG2 / A215 / Kue",
            "E / / Zha",
            "M / / Ang",
            "M / / Ang",
            "",
            "S / TH / Wues",
            "D / / Stra",
            "D / / Stra",
            "",
            "Robml / C008.2,3 /",
            "Robml / C008.2,3 /",
        ],
    )

    cal.add_events(
        "Tuesday",
        [
            "",
            "Inf2 / / Von",
            "Inf2 / / Von",
            "D / / Stra",
            "M / / Ang",
            "",
            "F / B209 / Ker,Mih",
            "F / B209 / Ker,Mih",
            "G / / Raf",
        ],
    )

    cal.add_events(
        "Wednesday",
        [
            "",
            "",
            "M / / Ang",
            "L / / Gub",
            "L / / Gub",
            "Mu2 / A209 / Kla",
        ],
    )

    cal.add_events(
        "Thursday",
        [
            "",
            "D / / Stra",
            "F / B209 / Ker,Mih",
            "E / / Zha",
            "E / / Zha",
            "",
            "",
            "G / / Raf",
            "B / / Zel",
            "B / / Zel",
        ],
    )

    cal.add_events(
        "Friday",
        [
            "S / Riw gr / Wues",
            "S / Riw gr / Wues",
            "RKE / / Cad",
            "L / / Gub",
            "Mu2 / A109 / Kla",
            "",
            "G / / Raf",
            "G / / Raf",
        ],
    )

    cal.write_file(output_file)
    print(f"Calendar wrote to {output_file} successfully")


if __name__ == "__main__":
    main()
