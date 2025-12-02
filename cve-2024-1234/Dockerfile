# Base image
FROM node:18-alpine

# Set working directory
WORKDIR /usr/src/app

# Copy package definition
COPY package*.json ./

# Install dependencies (including devDependencies if not specified otherwise)
RUN npm install

# Copy application source code
COPY . .

# Expose the application port
EXPOSE 8080

# VULNERABILITY: No USER instruction is present.
# The container defaults to 'root' user (UID 0).
# If the app is compromised, the attacker has root access to the container filesystem.
CMD ["npm", "start"]