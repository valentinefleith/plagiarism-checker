FROM node:18-alpine as build-stage

WORKDIR /app
COPY . .
RUN npm install
RUN npm run build

FROM nginx:stable-alpine as production-stage

COPY --from=build-stage /app/dist /usr/share/nginx/html


EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
