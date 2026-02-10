function analyze() {
  const logData = document.getElementById("logInput").value.trim().split("\n");
  let total = 0;
  let ipCount = {};

  logData.forEach(line => {
    const parts = line.split(" ");
    if (parts.length === 2) {
      const ip = parts[0];
      total++;

      ipCount[ip] = (ipCount[ip] || 0) + 1;
    }
  });

  let mostIP = "";
  let maxCount = 0;

  for (let ip in ipCount) {
    if (ipCount[ip] > maxCount) {
      maxCount = ipCount[ip];
      mostIP = ip;
    }
  }

  document.getElementById("total").textContent = total;
  document.getElementById("ip").textContent = mostIP;
}
