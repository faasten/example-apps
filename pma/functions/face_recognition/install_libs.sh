apk update \
    && apk add --no-cache \
        musl \
        jpeg jpeg-dev \
        libpng libpng-dev \
        giflib giflib-dev \
        openblas openblas-dev

cp -r /usr/lib/* /lib/* /app/out/lib
