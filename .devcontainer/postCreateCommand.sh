#!/bin/bash
set -e

echo "=== Logic101 Setup ==="

pip install --upgrade pip 2>/dev/null
pip install l101 2>/dev/null || pip install -e /workspaces/l101 2>/dev/null || true

echo ""
echo "Checking authentication..."
if l101 status > /dev/null 2>&1; then
    echo "Already authenticated."
else
    echo ""
    echo "Welcome to Logic101!"
    echo "Please run 'l101 login' to authenticate with GitHub."
    echo "This is required before you can pull problem sets or submit work."
    echo ""
fi

echo "Setup complete. Happy coding!"