#!/bin/sh

OMNI_VER=4.2.4
OMNI_BASE=omniORB-${OMNI_VER}
OMNI_TAR=${OMNI_BASE}.tar.bz2

OMPY_VER=4.2.4
OMPY_BASE=omniORBpy-${OMPY_VER}
OMPY_TAR=${OMPY_BASE}.tar.bz2

# omniORB
if [ ! -f ${OMNI_TAR} ]; then
    wget -O ${OMNI_TAR} https://sourceforge.net/projects/omniorb/files/omniORB/omniORB-4.2.4/omniORB-4.2.4.tar.bz2/download
fi

if [ ! -d ${OMNI_BASE} ]; then
    tar xvfj ${OMNI_TAR}
fi

mkdir -p ${OMNI_BASE}/build
cd ${OMNI_BASE}/build; ./../configure PYTHON=/usr/bin/python3  # PYTHON引数でpython3を指定. デフォルトで/usr/localにインストールされる.
cd build; make -j$(nproc)
sudo cd build; make install


# omniORBpy
if [ ! -f ${OMPY_TAR} ]; then
    wget -O ${OMPY_TAR} https://sourceforge.net/projects/omniorb/files/omniORBpy/${OMPY_BASE}/${OMPY_TAR}/download
fi

if [ ! -d ${OMPY_BASE} ]; then
    tar xvfj ${OMPY_TAR}
fi

mkdir -p ${OMPY_BASE}/build
cd ${OMPY_BASE}/build; ./../configure PYTHON=/usr/bin/python3  # omniORBと同じ
cd build; make -j$(nproc)
sudo cd build; make install
