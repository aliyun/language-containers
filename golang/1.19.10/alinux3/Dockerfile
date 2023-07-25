ARG BASE_OS=alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/alinux3

FROM ${BASE_OS}

ENV GOLANG_VERSION 1.19.10

RUN yum install -y golang-${GOLANG_VERSION}

ENV GOPATH /go

ENV PATH $GOPATH/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH
