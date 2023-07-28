ARG BUILDER=anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/golang:1.19.10-8.6

FROM ${BUILDER} as builder

ARG CACHEBUST=1

# check version
RUN if [[ "$(go version)" != "go version go${GOLANG_VERSION}"* ]]; then \
        echo >&2 "error: Golang version should start with 'go version go${GOLANG_VERSION}', got '$(go version)'"; \
        exit 1; \
    fi;

# RUN yum install -y git
# RUN git clone https://github.com/golang/go.git -b go${GOLANG_VERSION}

# golang tests
RUN cd /usr/local/go/src && \
    go tool dist test -rebuild -run="!syscall"

# Note:
#
# https://github.com/golang/go/commit/092671423cd95eaa6df93eb29442fef41504d097
# This patch doesn't get integrated into 1.19.10, so TestUnshareMountNameSpace etc. would fail.
