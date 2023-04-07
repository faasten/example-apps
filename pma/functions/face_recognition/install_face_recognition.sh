apk update \
    && apk add --no-cache \
        cmake \
        libstdc++ libgcc g++ \
        make \
        jpeg jpeg-dev \
        libpng libpng-dev \
        giflib giflib-dev \
        openblas \
        openblas-dev \
        python3 py3-pip python3-dev py3-wheel \
        git

su user -c 'pip3 install --upgrade --target out/package -r requirements.txt';
