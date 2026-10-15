import sys
from stats import read_valid, average_by_city, warmest_city

def main():
    lines = sys.stdin.read().splitlines()
    
    valid = read_valid(lines)
    total_parsed = len(valid)
    
    non_empty = [l for l in lines if l.strip()]
    total_skipped = len(non_empty) - total_parsed
    
    warm = warmest_city(valid)
    if warm:
        avg = average_by_city(valid)[warm]
    else:
        avg = 0.0
    
    print(total_parsed)
    print(total_skipped)
    print(f"{avg:.1f}")

if __name__ == "__main__":
    main()
