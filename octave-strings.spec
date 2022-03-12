%global octpkg strings

Summary:	Additional functions for manipulation and analysis of strings with Octave
Name:		octave-%{octpkg}
Version:	1.2.0
Release:	1
Source0:	https://downloads.sourceforge.net/octave/%{octpkg}-%{version}.tar.gz
# https://savannah.gnu.org/bugs/index.php?57000
Patch0:		err-instead-of-gripes.patch
# (debian)
Patch1:		build-against-octave-6.patch
# https://savannah.gnu.org/bugs/?61570
Patch2:		build-against-pcre2-mem-fix.patch
License:	GPLv3+ and BSD
Group:		Sciences/Mathematics
Url:		https://octave.sourceforge.io/%{octpkg}/

BuildRequires:	octave-devel >= 3.8.0
BuildRequires:	pkgconfig(libpcre)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
Additional functions for manipulation and analysis of strings with Octave.

This package is part of community Octave-Forge collection.

%files
%license COPYING
%doc NEWS
%dir %{octpkglibdir}
%{octpkglibdir}/*
%dir %{octpkgdir}
%{octpkgdir}/*

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove backup files
find . -name \*~ -delete

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

