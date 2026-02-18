#!/usr/bin/env python3

from datetime import datetime

from ical import ICAL

name = "KUE Stundenplan (Frühlingssemester 2026)"
output_file = "2026_spring.ics"


def main():
    start_date = datetime(2026, 2, 23)
    end_date = datetime(2026, 7, 12)
    cal = ICAL(name=name, start_date=start_date, end_date=end_date)
    cal.add_timezone_component()

    cal.add_events(
        "Monday",
        [
            "",
            "D / B207 / Stra",
            "BG2 / A216 / Kue",
            "BG2 / A216 / Kue",
            "Inf / C207 / Die",
            "Inf / C207 / Die",
            "",
            "E / B214 / Zha",
            "Mu / A019 / Kla,Pez",
            "Mu / A019 / Kla,Pez",
            "Robml / C008.2,3 /",
            "Robml / C008.2,3 /",
        ],
    )

    cal.add_events(
        "Tuesday",
        [
            "",
            "G / B113 / Raf",
            "M / C109 / But",
            "M / C109 / But",
            "F / B107 / Ker",
            "F / B107 / Ker",
            "",
            "L / B217 / Gub",
            "E / B209 / Zha",
            "D / B207 / Stra",
        ],
    )

    cal.add_events(
        "Wednesday",
        [
            "M / C109 / But",
            "M / C109 / But",
            "D / B210 / Stra",
            "D / B210 / Stra",
            "NF2 / C010 / Cos,Mar,But,Zel",
            "NF2 / C010 / Cos,Mar,But,Zel",
        ],
    )

    cal.add_events(
        "Thursday",
        [
            "",
            "",
            "F / B107 / Ker",
            "M / C109 / But",
            "S / TH / Wues",
            "",
            "",
            "L / A210 / Gub",
            "G / B113 / Raf",
            "G / B113 / Raf",
        ],
    )

    cal.add_events(
        "Friday",
        [
            "",
            "POOL",
            "G / B108 / Raf",
            "L / B208 / Gub",
            "RKE / B210 / Cad",
            "",
            "",
            "S / TH / Wues",
            "S / TH / Wues",
        ],
    )

    cal.write_file(output_file)
    print(f"Calendar wrote to {output_file} successfully")


if __name__ == "__main__":
    main()
