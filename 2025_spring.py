#!/usr/bin/env python3

from datetime import datetime

from ical import ICAL

name = "KUE Stundenplan (Frühlingssemester 2025)"
output_file = "2025_spring.ics"


def main():
    start_date = datetime(2025, 2, 24)
    end_date = datetime(2025, 7, 13)
    cal = ICAL(name=name, start_date=start_date, end_date=end_date)
    cal.add_timezone_component()

    # Monday (Montag)
    # --
    cal.add_event("Monday", "08:15", "F - A208 - Ker,Mih")
    cal.add_event("Monday", "09:10", "M - A208 - But")
    cal.add_event("Monday", "10:15", "M - A208 - But")
    cal.add_event("Monday", "11:10", "Ph - B009 - Cos")
    cal.add_event("Monday", "12:00", "B - B008 - Syr")
    # --
    cal.add_event("Monday", "13:40", "Gg - B109 - Jae")
    cal.add_event("Monday", "14:35", "E - A208 - Zha")
    cal.add_event("Monday", "15:30", "L - A208 - Gub")
    cal.add_event("Monday", "16:20", "Robml - C008.2 - Bar,Die")
    cal.add_event("Monday", "17:05", "Robml - C008.2 - Bar,Die")

    # Tuesday (Dienstag)
    cal.add_event("Tuesday", "07:25", "S - TH - Wues")
    cal.add_event("Tuesday", "08:15", "S - TH - Wues")
    cal.add_event("Tuesday", "09:10", "L - A208 - Gub")
    cal.add_event("Tuesday", "10:15", "M - A208 - But")
    # --
    cal.add_event("Tuesday", "12:00", "Mu - A019 - Kla")
    cal.add_event("Tuesday", "12:50", "Mu - A019 - Kla")
    cal.add_event("Tuesday", "13:40", "D - A208 - Stra")
    cal.add_event("Tuesday", "14:35", "D - A208 - Stra")
    # --
    # --
    # --

    # Wednesday (Mittwoch)
    cal.add_event("Wednesday", "07:25", "Rob2 - C008.3 - Gri")
    cal.add_event("Wednesday", "08:15", "Rob2 - C008.3 - Gri")
    cal.add_event("Wednesday", "09:10", "Ph - B009 - Cos")
    cal.add_event("Wednesday", "10:15", "Gg - B109 - Jae")
    # --

    # Thursday (Donnerstag)
    # --
    cal.add_event("Thursday", "08:15", "BG2 - A216 - Kue")
    cal.add_event("Thursday", "09:10", "BG2 - A216 - Kue")
    cal.add_event("Thursday", "10:15", "D - A208 - Stra")
    # --
    cal.add_event("Thursday", "12:00", "S - TH - Wues")
    # --
    cal.add_event("Thursday", "13:40", "M - A208 - But")
    cal.add_event("Thursday", "14:35", "RKE - A208 - Cad")
    cal.add_event("Thursday", "15:30", "E - A208-Zha / A209-Nor")
    # --
    # --

    # Friday (Freitag)
    # --
    # --
    cal.add_event("Friday", "09:10", "RKE - A208 - Cad")
    cal.add_event("Friday", "10:15", "L - A208 - Gub")
    cal.add_event("Friday", "11:10", "B - C010 - Syr")
    # --
    cal.add_event("Friday", "12:50", "Gg - B109 - Jae")
    cal.add_event("Friday", "13:40", "Gg - B109 - Jae")
    cal.add_event("Friday", "14:35", "F - A208 - Ker,Mih")
    cal.add_event("Friday", "15:30", "F - A208 - Ker,Mih")
    # --
    # --

    cal.write_file(output_file)
    print(f"Calendar wrote to {output_file} successfully")


if __name__ == "__main__":
    main()
