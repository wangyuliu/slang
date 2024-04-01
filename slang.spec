%bcond_with oniguruma

Name:		slang
Version:	2.3.3
Release:	2
Summary:	An interpreted language and programing library
License:	GPLv2+
URL:		https://www.jedsoft.org/slang/
Source0:	https://www.jedsoft.org/releases/slang/%{name}-%{version}.tar.bz2

Provides:       %{name}-slsh = %{version}-%{release}
Obsoletes:      %{name}-slsh < %{version}-%{release}

Patch0:		slang-sighuptest.patch

BuildRequires:	gcc libpng-devel zlib-devel

%description
S-Lang is a multi-platform programmer's library designed to allow
a developer to create robust multi-platform software. It provides
facilities required by interactive applications such as display/
screen management, keyboard input, keymaps, and so on.

%package     devel
Summary:     Files for %{name} development
Requires:    %{name}%{?_isa} = %{version}-%{release}

%description devel
Files for %{name} development

%package     help
Summary:     Help files for %{name}
BuildArch:   noarch

%description help
Help files for %{name}

%prep
%autosetup -n %{name}-%{version} -p1

sed -i '/^INSTALL_MODULE=/s/_DATA//' configure

%build
%configure --with-{png,z}lib=%{_libdir} --with-{png,z}inc=%{_includedir} --without-pcre

make RPATH="" install_doc_dir=%{_pkgdocdir} all

%install
make install-all RPATH="" INSTALL="install -p" DESTDIR=%{buildroot}

mkdir  %{buildroot}%{_includedir}/slang
for h in slang.h slcurses.h; do
    ln -s ../$h %{buildroot}%{_includedir}/slang/$h
done

%check
make check

%ldconfig_scriptlets

%files
%exclude %{_docdir}/{slang,slsh}
%exclude %{_libdir}/libslang.a
%{!?_licensedir:%global license %%doc}
%config(noreplace) %{_sysconfdir}/slsh.rc
%license COPYING
%doc NEWS slsh/doc/html/*.html
%{_libdir}/libslang.so.2*
%{_libdir}/%{name}
%{_bindir}/slsh
%{_datadir}/slsh

%files devel
%doc doc/text/*.txt doc/README doc/*.txt
%{_libdir}/libslang.so
%{_libdir}/pkgconfig/%{name}.pc
%{_includedir}/slang.h
%{_includedir}/slcurses.h
%{_includedir}/%{name}

%files help
%defattr(-,root,root)
%{_mandir}/man1/slsh.1*

%changelog
* Tue Apr 25 2023 fuanan <fuanan3@h-partners.com> - 2.3.3-2
- decouple from pcre

* Wed Jan 18 2023 fuanan <fuanan3@h-partners.com> - 2.3.3-1
- update version to 2.3.3

* Mon Aug 02 2021 chenyanpanHW <chenyanpan@huawei.com> - 2.3.2-9
- DESC: delete -Sgit from %autosetup, and delete BuildRequires git

* Wed Dec 25 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3.2-8
- Add provides of slang-slsh

* Thu Nov 21 2019 fangyufa <fangyufa1@huawei.com> - 2.3.2-7
- add buildrequires of git for x86_64 build

* Tue Sep 24 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3.2-6
- Remove unnecessary info in spec

* Mon Sep 16 2019 openEuler Buildteam <buildteam@openeuler.org> - 2.3.2-5
- Package init
