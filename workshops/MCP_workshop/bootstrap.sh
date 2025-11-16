#!/bin/bash

set -e  

echo "🚀 Starting MCP Workshop Bootstrap..."

# Update package lists
echo "📦 Updating package lists..."
apt-get update -y

# Install curl if not present (needed for installers)
echo "🔧 Installing curl..."
apt-get install -y curl

# Install Node.js and npm
echo "📦 Installing Node.js and npm..."
curl -fsSL https://deb.nodesource.com/setup_20.x | bash -
apt-get install -y nodejs

# Verify Node.js and npm installation
echo "✅ Node.js version: $(node --version)"
echo "✅ npm version: $(npm --version)"

# Install MCP Inspector globally
echo "📦 Installing MCP Inspector..."
npm install -g @modelcontextprotocol/inspector

# Install uv
echo "📦 Installing uv..."
curl -LsSf https://astral.sh/uv/install.sh | sh

# Add uv to PATH for current session
export PATH="$HOME/.cargo/bin:$PATH"

# Verify uv installation
echo "✅ uv version: $(uv --version)"

# Run uv sync to install Python dependencies
echo "📦 Running uv sync to install Python dependencies..."
uv sync

echo "✨ Bootstrap complete! All dependencies have been installed."
echo "🎯 You can now run the MCP workshop applications."
