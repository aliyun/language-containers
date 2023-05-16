ARG BUILDER=anolis-registry.cn-zhangjiakou.cr.aliyuncs.com/openanolis/tensorflow:1.15.5-8.6

FROM ${BUILDER} as builder

ARG CACHEBUST=1

# tensorflow sanity check
RUN python -c 'import tensorflow'
