FROM trustyboy/xxqg-python-env:latest as builder

RUN mkdir -p /data/XueQG/Config
    
COPY Config/Config.cfg /data/XueQG/Config/Config.cfg
COPY answers /data/XueQG/answers
COPY func /data/XueQG/func
COPY study /data/XueQG/study
COPY XueQG.py /data/XueQG/XueQG.py
COPY requirements.txt /data/XueQG/requirements.txt

ENV LIBRARY_PATH=/lib:/usr/lib

RUN cd /data/XueQG && pyinstaller -F XueQG.py

FROM trustyboy/xxqg-selenium-env:latest

RUN mkdir -p /data/XueQG/Config && cd /data/XueQG

COPY Config/Config.cfg /data/XueQG/Config/Config.cfg
COPY stealth.min.js /data/XueQG/stealth.min.js
COPY --from=builder /data/XueQG/dist/XueQG /data/XueQG/XueQG

WORKDIR /data/XueQG
ENTRYPOINT ["./XueQG"]
