ARG BUILDER=anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/python:3.11.1-8.6

FROM ${BUILDER} as builder

ARG CACHEBUST=1

# check version
RUN if [ "$(python --version)" != "Python ${PYTHON_VERSION}" ]; then \
        echo >&2 "error: Python version should be 'Python ${PYTHON_VERSION}', got '$(python --version)'"; \
        exit 1; \
    fi;

RUN yum install -y git

RUN git clone https://github.com/python/cpython.git -b v${PYTHON_VERSION}

# python tests
RUN cd cpython && \
    cp -r Lib/test /usr/local/lib/python* && \
    cp -r Lib/unittest/test /usr/local/lib/python*/unittest && \
    cp -r Lib/distutils/tests /usr/local/lib/python*/distutils && \
    cp -r Lib/idlelib/idle_test /usr/local/lib/python*/idlelib && \
    cp -r Lib/lib2to3/tests /usr/local/lib/python*/lib2to3/ && \
    cd /usr/local/lib/python* && \
    python -m test -x test_minidom -x test_venv

# Note:
# test_minidom needs Expat >= 2.4.5. But anolis only supports Expat 2.2.5 for now.
# See: https://github.com/python/cpython/pull/31453/files:
# Quote: "Make test suite support Expat >=2.4.5"

