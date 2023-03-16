ARG BUILDER=anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/node:16.17.1-nslt-8.6

FROM ${BUILDER} as builder

ARG CACHEBUST=1

USER root

# check version
RUN if [[ "$(node --version)" != "v${NODE_VERSION}" ]]; then \
        echo >&2 "error: Node version should be 'v${NODE_VERSION}', got '$(node --version)'"; \
        exit 1; \
    fi;

RUN yum install -y git python3 procps
RUN ln -s /usr/bin/python3 /usr/bin/python

RUN git clone https://github.com/nodejs/node.git -b v${NODE_VERSION}

# node tests
RUN cd node && \
    python3 tools/test.py --shell /usr/local/bin/node --skip-tests=test-child-process-stdio-overlapped,test-process-config,test-cluster-primary-error,test-cluster-primary-kill

