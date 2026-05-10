#!/bin/bash
set -e

echo "========================================="
echo "  Welcome to Logic101"
echo "========================================="
echo ""

pip install --upgrade pip 2>/dev/null
pip install l101 2>/dev/null || pip install -e /workspaces/l101 2>/dev/null || true

echo ""
echo "Checking authentication..."
if l101 status > /dev/null 2>&1; then
    echo "Already authenticated."
else
    echo ""
    echo "Welcome to Logic101!"
    echo ""
    echo "Before you start coding, authenticate with GitHub:"
    echo ""
    echo "  l101 login"
    echo ""
    echo "Then read the problems on the website:"
    echo "  https://logic101.dhritikrishna.me/psets/"
    echo ""
    echo "When ready, test and submit your work:"
    echo "  l101 test namaste.py"
    echo "  l101 submit pset0"
    echo ""
fi

echo "Setup complete. Happy coding!"