ARG BASE_OS=alibaba-cloud-linux-3-registry.cn-hangzhou.cr.aliyuncs.com/alinux3/alinux3

FROM ${BASE_OS}

ENV PYTHON_VERSION            3.8.12
ENV PYTHON_PIP_VERSION        19.3.1
ENV PYTHON_SETUPTOOLS_VERSION 41.6.0

RUN yum install -y \
        python38-${PYTHON_VERSION} \
        python38-pip-wheel-${PYTHON_PIP_VERSION} \
        python38-setuptools-wheel-${PYTHON_SETUPTOOLS_VERSION} && \
    yum clean all

CMD ["python3.8"]
