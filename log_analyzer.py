def analyze_log(file_name):
    total_requests = 0
    status_count = {}
    ip_count = {}

    with open(file_name, "r") as file:
        for line in file:
            parts = line.strip().split()
            if len(parts) != 2:
                continue   # skip invalid lines

            ip, status = parts
            total_requests += 1

            status_count[status] = status_count.get(status, 0) + 1
            ip_count[ip] = ip_count.get(ip, 0) + 1

    print("📊 LOG ANALYSIS REPORT")
    print("Total Requests:", total_requests)
    print("Status Code Count:", status_count)

    if ip_count:
        most_frequent_ip = max(ip_count, key=ip_count.get)
        print("Most Frequent IP:", most_frequent_ip)
    else:
        print("Most Frequent IP: N/A (no valid data)")


if __name__ == "__main__":
    analyze_log("sample.log")
