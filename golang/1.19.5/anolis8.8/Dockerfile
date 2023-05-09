ARG BASE_OS=openanolis/anolisos:8.8

FROM ${BASE_OS} as tire0

ARG TARGETPLATFORM

RUN yum install -y tar wget

RUN set -eux; \
    arch="$TARGETPLATFORM"; \
	url=; \
    case "$arch" in \
        'linux/amd64') \
			url='https://mirror.nju.edu.cn/golang/go1.19.5.linux-amd64.tar.gz'; \
			sha256='36519702ae2fd573c9869461990ae550c8c0d955cd28d2827a6b159fda81ff95'; \
            ;; \
        'linux/arm/v7') \
			url='https://mirror.nju.edu.cn/golang/go1.19.5.linux-arm64.tar.gz'; \
			sha256='fc0aa29c933cec8d76f5435d859aaf42249aa08c74eb2d154689ae44c08d23b3'; \
            ;; \
        'linux/arm64') \
			url='https://mirror.nju.edu.cn/golang/go1.19.5.linux-arm64.tar.gz'; \
			sha256='fc0aa29c933cec8d76f5435d859aaf42249aa08c74eb2d154689ae44c08d23b3'; \
            ;; \
        *) echo >&2 "error: unsupported architecture '$arch'"; exit 1 ;; \
    esac; \
    wget -O go.tgz "$url" --progress=dot:giga; \
	echo "$sha256 *go.tgz" | sha256sum -c -; \
    tar -C /usr/local -xzf /go.tgz

FROM ${BASE_OS}

# install cgo-related dependencies
RUN set -eux; \
    yum install -y gcc gcc-c++ glibc-devel make pkg-config; \
    yum clean all

ENV PATH /usr/local/go/bin:$PATH

ENV GOLANG_VERSION 1.19.5

COPY --from=tire0 /usr/local/go /usr/local/go

RUN go version

ENV GOPATH /go
ENV PATH $GOPATH/bin:$PATH
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"
WORKDIR $GOPATH
