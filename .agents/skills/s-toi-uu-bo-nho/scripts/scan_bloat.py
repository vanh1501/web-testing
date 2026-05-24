import os
import argparse
import math

def scan_bloat(directory, threshold_kb=15.0):
    bloated_files = []
    
    if not os.path.isdir(directory):
        print(f"ERROR: Directory '{directory}' does not exist.")
        return []
        
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(('.md', '.yaml', '.json')):
                file_path = os.path.join(root, file)
                try:
                    size_bytes = os.path.getsize(file_path)
                    size_kb = size_bytes / 1024.0
                    if size_kb > threshold_kb:
                        bloated_files.append((file_path, size_kb))
                except Exception as e:
                    pass
                    
    # Sort descending by size
    bloated_files.sort(key=lambda x: x[1], reverse=True)
    return bloated_files

def main():
    parser = argparse.ArgumentParser(description="Scan for Token Bloat (Files > Threshold)")
    parser.add_argument('path', type=str, help="Directory to scan")
    parser.add_argument('--threshold', type=float, default=15.0, help="Max file size in KB (default: 15.0)")
    
    args = parser.parse_args()
    
    print(f"Scanning [{args.path}] for files > {args.threshold} KB...")
    results = scan_bloat(args.path, args.threshold)
    
    if not results:
        print("[SUCCESS] No bloated files found. System is healthy!")
        return 0
        
    print(f"[FOUND] {len(results)} files violating the size parameter:")
    print("-" * 60)
    for path, size in results:
        print(f"{size:8.2f} KB | {path}")
    print("-" * 60)
    return 1

if __name__ == "__main__":
    main()
