############ TARGET ############
FROM node

RUN npm install -g quicktype

COPY languages ./languages/
COPY objects ./objects/
COPY generate_types.sh .

RUN ./generate_types.sh
