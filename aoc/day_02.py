"""Processing for Day 02"""

def red_nosed_reports(data: str, dampener: bool) -> int:
    """Take the data and return the appropriate value"""

    safe = 0

    for report_str in data.splitlines():
        report = [int(level) for level in report_str.split(" ")]

        reports = [report]

        if dampener:
            for idx in range(1, len(report)):
                reports.append(report[:idx - 1] + report[idx:])
            reports.append(report[:-1])

        for report in reports:
            diff = report[0] - report[1]
            diff_abs = abs(diff)

            if diff_abs < 1 or diff_abs > 3:
                continue

            sign = diff // diff_abs

            for idx in range(2, len(report)):
                diff = report[idx-1] - report[idx]
                diff_abs = abs(diff)

                if diff_abs < 1 or diff_abs > 3:
                    break
                elif diff // diff_abs != sign:
                    break
            else:
                safe += 1
                break

    return safe
