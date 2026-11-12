import logstats

def main():
    try:
        filename = input().strip()
    except EOFError:
        return
        
    if not filename:
        return

    with open(filename, encoding="utf-8") as log:
        counts = logstats.count_levels(log)

    with open(filename, encoding="utf-8") as log:
        errors = logstats.top_errors(log, 3)

    total_lines = sum(counts.values())
    error_count = counts.get("ERROR", 0)
    broken_count = counts.get("BROKEN", 0)

    print(total_lines)
    print(error_count)
    print(broken_count)

    report_text = logstats.format_report(counts, errors)
    with open("report.txt", "w", encoding="utf-8") as out_file:
        out_file.write(report_text)

if __name__ == "__main__":
    main()
