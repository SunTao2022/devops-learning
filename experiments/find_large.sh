

#!/bin/bash
files=$(find /tmp -size +1M 2>/dev/null)
echo "$files" | xargs -I{} ls -lh {} 2>/dev/null
echo "---"
echo "Total: $(echo "$files" | wc -l) files"