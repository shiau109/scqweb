FROM node:18-alpine

WORKDIR /app

# Copy dependency definitions first for better cache
COPY package*.json ./

# Install dependencies including @vitejs/plugin-react
RUN npm install

# Copy the rest of the app
COPY . .

# Expose Vite's default port
EXPOSE 5173

# Run Vite with host enabled
CMD ["npm", "run", "dev", "--", "--host"]
