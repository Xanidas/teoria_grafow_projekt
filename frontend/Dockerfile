FROM    docker.io/library/node:22.11 AS build
WORKDIR /app
COPY    . .
RUN     rm -rf package-lock.json \
    &&  npm install --legacy-peer-deps \
    &&  npm run build --prod

FROM    docker.io/library/nginx:1.21-alpine
COPY    --from=build /app/dist/frontend/browser/ /usr/share/nginx/html/
RUN     rm -rf /etc/nginx/nginx.conf  \
    &&  rm -rf /etc/nginx/conf.d
COPY    dockerfile-assets/nginx.conf  /etc/nginx/
COPY    dockerfile-assets/server.conf /etc/nginx/
EXPOSE  8080
ENV     NGINX_OPTIONS=""
WORKDIR /usr/share/nginx/html
RUN     chmod 664 /usr/share/nginx/html/assets/env.js
CMD     ["/bin/sh",  "-c",  "envsubst < /usr/share/nginx/html/assets/env.template.js > /usr/share/nginx/html/assets/env.js && exec nginx -g 'daemon off;'"]
