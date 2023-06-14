#!/bin/bash


# echo "Initializing container..."
UNOCONV_PATH="/usr/bin/unoconv"

# unoconvファイルの1行目を削除
sed -i '1d' "$UNOCONV_PATH"

# 新しい1行目を追加
sed -i '1i #!/usr/bin/python3' "$UNOCONV_PATH"