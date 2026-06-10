# Linux Practice — do each task in your terminal
# Run: source experiments/linux_practice.sh  (or type commands directly)

echo "===== Task 1: Where am I? ====="
# Type: pwd
# Expected: /c/Users/Tao/devops-learning
pwd

echo ""
echo "===== Task 2: List files ====="
# Type: ls -la  (what's the .git directory?)
ls -la

echo ""
echo "===== Task 3: Make a directory tree ====="
# Type: mkdir -p my-project/src my-project/tests my-project/docs
mkdir -p my-project/src my-project/tests my-project/docs
ls -R my-project/

echo ""
echo "===== Task 4: Create files ====="
# Type: touch my-project/src/app.py my-project/tests/test_app.py my-project/docs/README.md
touch my-project/src/app.py my-project/tests/test_app.py my-project/docs/README.md
ls -R my-project/

echo ""
echo "===== Task 5: Clean up ====="
# Type: rm -r my-project
rm -r my-project
echo "Cleaned!"
