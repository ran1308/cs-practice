# проверки добавлены
def parse_record(line: str) -> dict:
    parts = line.split(";")
    if len(parts) != 3:
        raise ValueError("Ожидалось 3 поля")
    
    city, temp_str, date = parts
    
    if not city.strip() or not date.strip():
        raise ValueError("Пустой город или дата")
    
    try:
        temp = float(temp_str)
    except ValueError:
        raise ValueError("Температура не число")
    
    return {"city": city.strip(), "temperature": temp, "date": date.strip()}


def read_valid(lines: list[str]) -> list[dict]: # обработка ошибок
    records = []
    for line in lines:
        if not line.strip():
            continue
        try:
            records.append(parse_record(line))
        except ValueError:
            pass
    return records


def average_by_city(records: list[dict]) -> dict:
    totals = {}
    counts = {}
    for rec in records:
        c = rec["city"]
        totals[c] = totals.get(c, 0.0) + rec["temperature"]
        counts[c] = counts.get(c, 0) + 1
    
    result = {}
    for c in totals:
        result[c] = round(totals[c] / counts[c], 1)
    return result


def warmest_city(records: list[dict]) -> str:
    if not records:
        return ""
    avg = average_by_city(records)
    if not avg:
        return ""
    best = sorted(avg.items(), key=lambda x: (-x[1], x[0]))[0][0]
    return best
# добавил проверки в parse_record
# реализовал обработку ошибок в read_valid
