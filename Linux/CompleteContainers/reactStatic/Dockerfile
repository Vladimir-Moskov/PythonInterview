FROM node:latest
WORKDIR /app
COPY . .
RUN npm ci && npm run build

# you could totally use nginx:alpine here too
FROM nginx:latest
COPY --from=0 /app/build /usr/share/nginx/html
