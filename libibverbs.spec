#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libibverbs
Version  : 1.2.0
Release  : 2
URL      : https://www.openfabrics.org/downloads/verbs/libibverbs-1.2.0.tar.gz
Source0  : https://www.openfabrics.org/downloads/verbs/libibverbs-1.2.0.tar.gz
Summary  : A library for direct userspace use of RDMA (InfiniBand/iWARP) hardware
Group    : Development/Tools
License  : BSD-2-Clause GPL-2.0
Requires: libibverbs-bin
Requires: libibverbs-lib
Requires: libibverbs-doc
BuildRequires : pkgconfig(libnl-3.0)

%description
libibverbs is a library that allows userspace processes to use RDMA
"verbs" as described in the InfiniBand Architecture Specification and
the RDMA Protocol Verbs Specification.  This includes direct hardware
access from userspace to InfiniBand/iWARP adapters (kernel bypass) for
fast path operations.

For this library to be useful, a device-specific plug-in module should
also be installed.

%package bin
Summary: bin components for the libibverbs package.
Group: Binaries

%description bin
bin components for the libibverbs package.


%package dev
Summary: dev components for the libibverbs package.
Group: Development
Requires: libibverbs-lib
Requires: libibverbs-bin
Provides: libibverbs-devel

%description dev
dev components for the libibverbs package.


%package doc
Summary: doc components for the libibverbs package.
Group: Documentation

%description doc
doc components for the libibverbs package.


%package lib
Summary: lib components for the libibverbs package.
Group: Libraries

%description lib
lib components for the libibverbs package.


%prep
%setup -q -n libibverbs-1.2.0

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/ibv_asyncwatch
/usr/bin/ibv_devices
/usr/bin/ibv_devinfo
/usr/bin/ibv_rc_pingpong
/usr/bin/ibv_srq_pingpong
/usr/bin/ibv_uc_pingpong
/usr/bin/ibv_ud_pingpong
/usr/bin/ibv_xsrq_pingpong

%files dev
%defattr(-,root,root,-)
/usr/include/infiniband/arch.h
/usr/include/infiniband/driver.h
/usr/include/infiniband/kern-abi.h
/usr/include/infiniband/marshall.h
/usr/include/infiniband/opcode.h
/usr/include/infiniband/sa-kern-abi.h
/usr/include/infiniband/sa.h
/usr/include/infiniband/verbs.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/man/man1/*
%doc /usr/share/man/man3/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
