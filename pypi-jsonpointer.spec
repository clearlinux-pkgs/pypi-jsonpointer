#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-jsonpointer
Version  : 2.2
Release  : 57
URL      : https://files.pythonhosted.org/packages/29/7f/e6b5930e6dd1f461ad412dfc40bc94e5235011f6bbf73cafa8074617c203/jsonpointer-2.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/29/7f/e6b5930e6dd1f461ad412dfc40bc94e5235011f6bbf73cafa8074617c203/jsonpointer-2.2.tar.gz
Summary  : Identify specific nodes in a JSON document (RFC 6901)
Group    : Development/Tools
License  : BSD-3-Clause
Requires: pypi-jsonpointer-bin = %{version}-%{release}
Requires: pypi-jsonpointer-license = %{version}-%{release}
Requires: pypi-jsonpointer-python = %{version}-%{release}
Requires: pypi-jsonpointer-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
Provides: jsonpointer
Provides: jsonpointer-python
Provides: jsonpointer-python3

%description
python-json-pointer
===================
[![PyPI version](https://img.shields.io/pypi/v/jsonpointer.svg)](https://pypi.python.org/pypi/jsonpointer/)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/jsonpointer.svg)](https://pypi.python.org/pypi/jsonpointer/)
[![Build Status](https://travis-ci.org/stefankoegl/python-json-pointer.svg?branch=master)](https://travis-ci.org/stefankoegl/python-json-pointer)
[![Coverage Status](https://coveralls.io/repos/stefankoegl/python-json-pointer/badge.svg?branch=master)](https://coveralls.io/r/stefankoegl/python-json-pointer?branch=master)

%package bin
Summary: bin components for the pypi-jsonpointer package.
Group: Binaries
Requires: pypi-jsonpointer-license = %{version}-%{release}

%description bin
bin components for the pypi-jsonpointer package.


%package license
Summary: license components for the pypi-jsonpointer package.
Group: Default

%description license
license components for the pypi-jsonpointer package.


%package python
Summary: python components for the pypi-jsonpointer package.
Group: Default
Requires: pypi-jsonpointer-python3 = %{version}-%{release}

%description python
python components for the pypi-jsonpointer package.


%package python3
Summary: python3 components for the pypi-jsonpointer package.
Group: Default
Requires: python3-core
Provides: pypi(jsonpointer)

%description python3
python3 components for the pypi-jsonpointer package.


%prep
%setup -q -n jsonpointer-2.2
cd %{_builddir}/jsonpointer-2.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1641449760
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
python tests.py
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-jsonpointer
cp %{_builddir}/jsonpointer-2.2/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-jsonpointer/0305317c0f694ba11e8f059938fd0c880356e7bc
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/jsonpointer

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-jsonpointer/0305317c0f694ba11e8f059938fd0c880356e7bc

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
