ARG BASE_OS=alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/alinux3

FROM ${BASE_OS}

RUN set -eux; \
    if [ "$(uname -m)" == "aarch64" ]; then \
        yum install -y epel-release; \
        yum install -y hdf5 lapack blas; \
    fi; \
	yum install -y python3-pip; \
    yum clean all; \
    rm -rf /var/cache/yum; \
    rm -rf /var/lib/yum/yumdb; \
    rm -rf /var/lib/yum/history

RUN set -eux; \
    python3 -m pip install --no-cache-dir -U pip; \
    python3 -m pip install --no-cache-dir --prefer-binary --extra-index=https://py-index.oss-cn-beijing.aliyuncs.com/simple/ tensorflow==1.15.5
