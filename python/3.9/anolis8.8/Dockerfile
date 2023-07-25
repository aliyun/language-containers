ARG BASE_OS=openanolis/anolisos:8.8

FROM ${BASE_OS}

ENV PYTHON_VERSION            3.9.16
ENV PYTHON_PIP_VERSION        20.2.4
ENV PYTHON_SETUPTOOLS_VERSION 50.3.2

RUN yum install -y \
        python39-${PYTHON_VERSION} \
        python39-pip-wheel-${PYTHON_PIP_VERSION} \
        python39-setuptools-wheel-${PYTHON_SETUPTOOLS_VERSION} && \
    yum clean all

CMD ["python3.9"]
