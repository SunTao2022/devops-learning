#!/bin/bash

# System Health Check

# 1. Disk
path="${1:-/mnt/c}"
usage=$(df -h "$path" | tail -1 | awk '{print $5}' | tr -d '%')
echo "Disk: ${usage}%"
if [ "$usage" -gt 80 ]; then
    echo "⚠️  Warning: Disk over 80%"
else
    echo "✅  Disk OK"
fi
echo ""

# 2. Memory
m_total=$(free -m | grep Mem | awk '{print $2}')
m_avail=$(free -m | grep Mem | awk '{print $7}')
m_usage=$(( (m_total - m_avail) * 100 / m_total ))
echo "Memory: ${m_usage}%"
if [ "$m_usage" -gt 90 ]; then
    echo "⚠️  Warning: Memory over 90%"
else
    echo "✅  Memory OK"
fi
echo ""

# 3. Uptime
echo "Uptime: $(uptime -p)"
echo ""

# 4. Load
load=$(uptime | awk -F'load average:' '{print $2}' | cut -d',' -f1 | tr -d ' ')
echo "Load: $load"
load_int=$(echo "$load" | cut -d'.' -f1)
if [ "$load_int" -gt 2 ]; then
    echo "⚠️  Warning: Load high"
else
    echo "✅  Load OK"
fi
