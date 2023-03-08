ARG BASE_OS=alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/alinux3

FROM ${BASE_OS} as builder

RUN yum install -y tar xz

ENV NODE_VERSION 16.17.1
ENV YARN_VERSION 1.22.19
ARG NODE_NAME=node-v${NODE_VERSION}
ARG YARN_NAME=yarn-v${YARN_VERSION}

ARG NODE_SRC_URL=https://language-containers.oss-cn-hangzhou.aliyuncs.com/node/node-v${NODE_VERSION}.tar.xz
ARG NODE_SRC_SHA256="00a65f7c2cbcc2dcbb6f8fc1d6acae673360ca1cb5ae09cb4ff36f8446bca4d3"
ARG YARN_BIN_URL=https://language-containers.oss-cn-hangzhou.aliyuncs.com/node/yarn-v${YARN_VERSION}.tar.gz
ARG YARN_BIN_SHA256="732620bac8b1690d507274f025f3c6cfdc3627a84d9642e38a07452cc00e0f2e"

RUN curl -LfsSo /${NODE_NAME}.tar.xz ${NODE_SRC_URL}; \
    echo "${NODE_SRC_SHA256} /${NODE_NAME}.tar.xz" | sha256sum -c -; \
    tar xf /${NODE_NAME}.tar.xz;
WORKDIR /${NODE_NAME}

RUN yum install -y python3 gcc-c++ make

RUN ./configure --prefix=/node; \
    make -j4 install;

ARG NODE_NAME=node-${NODE_VERSION}

RUN curl -LfsSo ${YARN_NAME}.tar.gz ${YARN_BIN_URL}; \
    echo "${YARN_BIN_SHA256} ${YARN_NAME}.tar.gz" | sha256sum -c -; \
    rm -rf /opt && mkdir /opt; \
    tar -xzf ${YARN_NAME}.tar.gz -C /opt/;

FROM ${BASE_OS}

ENV NODE_VERSION 16.17.1
ENV YARN_VERSION 1.22.19
ARG YARN_NAME=yarn-v${YARN_VERSION}

RUN groupadd -g 1000 node \
    && adduser -u 1000 -g node -s /bin/sh node

COPY --from=builder /node /usr/local
COPY --from=builder /opt /opt

RUN ln -s /opt/${YARN_NAME}/bin/yarn /usr/local/bin/yarn \
    && ln -s /opt/${YARN_NAME}/bin/yarnpkg /usr/local/bin/yarnpkg

USER node
