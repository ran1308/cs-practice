def count_by_extension(paths: list[str]) -> dict[str, int]:
    counts = {}
    for path in paths:
        dot_index = path.rfind('.')
        slash_index = path.rfind('/')
        
        if dot_index == -1 or dot_index < slash_index:
            ext = ""
        else:
            ext = path[dot_index + 1:].lower()
            
        counts[ext] = counts.get(ext, 0) + 1
    return counts


def deepest_path(paths: list[str]) -> str:
    if not paths:
        return ""
        
    sorted_paths = sorted(paths, key=lambda x: (-x.count('/'), x))
    return sorted_paths[0]


def human_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        return f"{n_bytes} Б"
        
    units = ["КБ", "МБ", "ГБ", "ТБ"]
    size = float(n_bytes)
    
    for unit in units:
        size /= 1024.0
        if size < 1024 or unit == units[-1]:
            if size.is_integer():
                return f"{int(size)} {unit}"
            else:
                return f"{size:.1f} {unit}"
