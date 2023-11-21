FROM node:18-alpine

WORKDIR /react/

COPY hello-world/public/ /react/public
COPY hello-world/src/ /react/src
COPY hello-world/package.json /react/

EXPOSE 3000

RUN npm install

CMD ["npm", "start"]
