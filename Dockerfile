FROM alpine:3.17.0
ENV TZ Asia/Shanghai
ENV LC_ALL=zh_CN.UTF-8

RUN sed -i 's/dl-cdn.alpinelinux.org/mirrors.aliyun.com/g' /etc/apk/repositories && \
    apk update && \
    apk add --no-cache tzdata && cp /usr/share/zoneinfo/${TZ} /etc/localtime && echo ${TZ} > /etc/timezone && \
    apk add --no-cache ttf-dejavu fontconfig && mkfontscale && mkfontdir && fc-cache && \
    apk add --no-cache zbar && \
    apk add --no-cache chromium=107.0.5304.121-r0 && \
    apk add --no-cache chromium-chromedriver=107.0.5304.121-r0 && \
    sed -i "s/\$cdc_/\$abc_/" /usr/lib/chromium/chromedriver && \
    rm -rf /var/cache/apk/* && \
    mkdir -p /data/XueQG/Config && \
    cd /data/XueQG

COPY Config/Config.cfg /data/XueQG/Config/Config.cfg
COPY dist/XueQG /data/XueQG/XueQG

WORKDIR /data/XueQG
ENTRYPOINT ["./XueQG"]
