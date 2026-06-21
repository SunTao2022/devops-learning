#!/bin/sh

disk=$1

usage=$(df -h "$disk"| tail -1 | awk '{print $5}' | tr -d '%')
echo "Disk: ${usage}%"
if [ "$usage" -gt 80 ]; then
    echo "⚠️ Warning: Disk over 80%"
else
    echo "✅ Disk OK"
fi


# 第一步：用变量存数字
m_total=$(free -m | grep Mem | awk '{print $2}')  # 总内存
m_avail=$(free -m | grep Mem | awk '{print $7}')  # 可用内存

# 第二步：用 $(( )) 做整数运算
M_usage=$(( (m_total - m_avail) * 100 / m_total ))
if [ "$M_usage" -gt 90 ]; then
    echo "⚠️ Warning: Memory over 90%"
else
    echo "✅ Memory OK"
fi

echo "$(uptime -p)"

C_usage=$(uptime | awk -F'load average:' '{print $2}' | cut -d',' -f1 | tr -d ' ')
echo "load: $C_usage"
int_C_usage=$(echo "$C_usage" | cut -d'.' -f1)

if [ "$int_C_usage" -gt 2 ]; then
    echo "⚠️ Load over 2"
else
    echo "✅ Load OK"
fi
