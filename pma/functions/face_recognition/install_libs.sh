apk update \
    && apk add --no-cache \
        musl \
        jpeg jpeg-dev \
        libpng libpng-dev \
        giflib giflib-dev \
        openblas openblas-dev

cp -r /usr/lib/* /lib/ld-musl-x86_64.so.1 /lib/libc.musl-x86_64.so.1 /app/out/lib
