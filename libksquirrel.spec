%bcond clang 1
%bcond ghostscript 1
%bcond djvu 1
%bcond xmedcon 0
%bcond svg 1
%bcond jasper 1
%bcond freetype 1
%bcond pict 0

# BUILD WARNING:
#  Remove qt-devel and qt3-devel and any kde*-devel on your system !
#  Having KDE libraries may cause FTBFS here !

# TDE variables
%define tde_epoch 2
%if "%{?tde_version}" == ""
%define tde_version 14.1.5
%endif
%define pkg_rel 2

%define tde_pkg libksquirrel

%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%define _debugsource_template %{nil}

%define tarball_name %{tde_pkg}-trinity


Name:		trinity-%{tde_pkg}
Epoch:		%{tde_epoch}
Version:	0.8.0
Release:	%{?tde_version}_%{?!preversion:%{pkg_rel}}%{?preversion:0_%{preversion}}%{?dist}
Summary:	Trinity image viewer
Group:		System/Libraries
URL:		http://www.trinitydesktop.org/

License:	GPLv2+

#Vendor:		Trinity Desktop
#Packager:	Francois Andriot <francois.andriot@free.fr>

Prefix:			/opt/trinity

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/libraries/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:	%{name}-rpmlintrc

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{prefix}/%{_lib}"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{prefix}"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{prefix}/share"
BuildOption:    -DINCLUDE_INSTALL_DIR="%{prefix}/include"
BuildOption:    -DLIB_INSTALL_DIR="%{prefix}/%{_lib}"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON -DBUILD_DICOM=OFF
BuildOption:    -DBUILD_PICT=%{!?with_pict:OFF}%{?with_pict:ON}
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}


BuildRequires:	trinity-tdelibs-devel >= %{tde_version}

BuildRequires:	desktop-file-utils

%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# libtool, I guess...
BuildRequires: libtool
BuildRequires:	%{_lib}ltdl-devel

# TRANSFIG support
BuildRequires:	transfig

# GHOSTSCRIPT support
%{?with_ghostscript:BuildRequires:	ghostscript}

# GETTEXT support
BuildRequires:	gettext
BuildRequires:	gettext-devel

# LCMS support
BuildRequires:  pkgconfig(lcms)

# OPENEXR support
BuildRequires:  pkgconfig(OpenEXR)

# TIFF support
BuildRequires:  pkgconfig(libtiff-4)

# GIF support
BuildRequires: %{_lib}gif-devel

# MNG support
BuildRequires:  pkgconfig(libmng)

# DJVU support
%{?with_djvu:BuildRequires:	djvulibre}

# XMEDCON support
%if %{with xmedcon}
BuildRequires:	xmedcon
BuildRequires:	xmedcon-devel
%endif

# RSVG support
%{?with_svg:BuildRequires:  librsvg}

# JASPER support
%{?with_jasper:BuildRequires:  pkgconfig(jasper)}

# FREETYPE support
%{?with_freetype:BuildRequires:  pkgconfig(freetype2)}

# WMF support
BuildRequires:  pkgconfig(libwmf)

# XML2 support
BuildRequires:	pkgconfig(libxml-2.0)

# NETPBM support
BuildRequires:	netpbm

BuildRequires:  x11-proto-devel

%description
This package contains the runtime libraries for KSquirrel.

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING LICENSE README
%dir %{prefix}/%{_lib}/ksquirrel-libs
%{prefix}/%{_lib}/ksquirrel-libs/libkls_avs.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_avs.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_bmp.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_bmp.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_camera.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_camera.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_cut.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_cut.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dds.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dds.so.0.8.0
%if %{with xmedcon}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dicom.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dicom.so.0.8.0
%endif
%if %{with djvu}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_djvu.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_djvu.so.0.8.0
%endif
%if %{with ghostscript}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_eps.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_eps.so.0.8.0
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fig.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fig.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fli.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fli.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_gif.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_gif.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_hdr.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_hdr.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ico.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ico.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_iff.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_iff.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jbig.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jbig.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg2000.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg2000.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_koala.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_koala.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_leaf.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_leaf.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_lif.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_lif.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ljpeg.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ljpeg.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mac.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mac.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mdl.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mdl.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mng.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mng.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_msp.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_msp.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mtv.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mtv.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_neo.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_neo.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_openexr.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_openexr.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pcx.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pcx.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi1.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi1.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi3.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi3.so.0.8.0
%if %{with pict}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pict.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pict.so.0.8.0
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pix.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pix.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_png.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_png.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pnm.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pnm.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psd.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psd.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psp.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psp.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pxr.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pxr.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ras.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ras.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_rawrgb.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_rawrgb.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sct.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sct.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sgi.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sgi.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sun.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sun.so.0.8.0
%if %{with svg}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_svg.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_svg.so.0.8.0
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tga.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tga.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tiff.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tiff.so.0.8.0
%if %{with freetype}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ttf.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ttf.so.0.8.0
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_utah.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_utah.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wal.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wal.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wbmp.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wbmp.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wmf.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wmf.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xbm.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xbm.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcf.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcf.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcur.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcur.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xim.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xim.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xpm.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xpm.so.0.8.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xwd.so.0
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xwd.so.0.8.0
%{prefix}/%{_lib}/libksquirrel-libs-png.so.0
%{prefix}/%{_lib}/libksquirrel-libs-png.so.0.8.0
%{prefix}/%{_lib}/libksquirrel-libs.so.0
%{prefix}/%{_lib}/libksquirrel-libs.so.0.8.0
%dir %{prefix}/share/ksquirrel-libs
%{prefix}/share/ksquirrel-libs/libkls_camera.so.ui
%if %{with djvu}
%{prefix}/share/ksquirrel-libs/libkls_djvu.so.ui
%endif
%if %{with svg}
%{prefix}/share/ksquirrel-libs/libkls_svg.so.ui
%endif
%{prefix}/share/ksquirrel-libs/libkls_tiff.so.ui
%{prefix}/share/ksquirrel-libs/libkls_xcf.so.ui
%{prefix}/share/ksquirrel-libs/rgbmap
%{prefix}/share/man/man1/ksquirrel-libs-camera2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-dcraw.1
%{prefix}/share/man/man1/ksquirrel-libs-dicom2png.1
%{prefix}/share/man/man1/ksquirrel-libs-fig2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-iff2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-leaf2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-ljpeg2ppm-s.1
%{prefix}/share/man/man1/ksquirrel-libs-ljpeg2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-mac2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-neo2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-pi12ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-pi32ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-svg2png.1
%{prefix}/share/man/man1/ksquirrel-libs-ttf2pnm.1
%{prefix}/share/man/man1/ksquirrel-libs-utah2ppm.1
%{prefix}/share/man/man1/ksquirrel-libs-xcf2pnm.1
%{prefix}/share/man/man1/ksquirrel-libs-xim2ppm.1

##########

%package devel
Group:		Development/Libraries/Other
Summary:	Trinity image viewer
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development libraries for KSquirrel.

%files devel
%defattr(-,root,root,-)
%dir %{prefix}/include/ksquirrel-libs
%{prefix}/include/ksquirrel-libs/error.h
%{prefix}/include/ksquirrel-libs/fileio.h
%{prefix}/include/ksquirrel-libs/fmt_codec_base.h
%{prefix}/include/ksquirrel-libs/fmt_defs.h
%{prefix}/include/ksquirrel-libs/fmt_types.h
%{prefix}/include/ksquirrel-libs/fmt_utils.h
%{prefix}/include/ksquirrel-libs/ksquirrel_libs_export.h
%{prefix}/include/ksquirrel-libs/settings.h
%{prefix}/%{_lib}/ksquirrel-libs/libkls_avs.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_avs.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_bmp.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_bmp.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_camera.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_camera.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_cut.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_cut.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dds.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dds.so
%if %{with xmedcon}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dicom.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_dicom.so
%endif
%if %{with djvu}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_djvu.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_djvu.so
%endif
%if %{with ghostscript}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_eps.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_eps.so
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fig.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fig.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fli.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_fli.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_gif.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_gif.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_hdr.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_hdr.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ico.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ico.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_iff.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_iff.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jbig.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jbig.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg2000.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_jpeg2000.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_koala.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_koala.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_leaf.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_leaf.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_lif.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_lif.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ljpeg.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ljpeg.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mac.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mac.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mdl.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mdl.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mng.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mng.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_msp.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_msp.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mtv.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_mtv.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_neo.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_neo.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_openexr.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_openexr.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pcx.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pcx.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi1.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi1.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi3.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pi3.so
%if %{with pict}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pict.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pict.la
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pix.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pix.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_png.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_png.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pnm.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pnm.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psd.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psd.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psp.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_psp.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pxr.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_pxr.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ras.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ras.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_rawrgb.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_rawrgb.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sct.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sct.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sgi.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sgi.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sun.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_sun.so
%if %{with svg}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_svg.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_svg.so
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tga.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tga.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tiff.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_tiff.so
%if %{with freetype}
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ttf.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_ttf.so
%endif
%{prefix}/%{_lib}/ksquirrel-libs/libkls_utah.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_utah.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wal.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wal.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wbmp.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wbmp.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wmf.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_wmf.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xbm.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xbm.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcf.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcf.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcur.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xcur.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xim.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xim.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xpm.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xpm.so
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xwd.la
%{prefix}/%{_lib}/ksquirrel-libs/libkls_xwd.so
%{prefix}/%{_lib}/libksquirrel-libs-png.la
%{prefix}/%{_lib}/libksquirrel-libs-png.so
%{prefix}/%{_lib}/libksquirrel-libs.la
%{prefix}/%{_lib}/libksquirrel-libs.so
%{prefix}/%{_lib}/pkgconfig/ksquirrellibs.pc
%{prefix}/share/doc/ksquirrel-libs/

##########

%package tools
Summary:	Trinity image viewer
Group:		System/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description tools
This package contains the tools for KSquirrel.

%files tools
%defattr(-,root,root,-)
%{prefix}/bin/ksquirrel-libs-camera2ppm
%{prefix}/bin/ksquirrel-libs-dcraw
%if %{with xmedcon}
%{prefix}/bin/ksquirrel-libs-dicom2png
%endif
%{prefix}/bin/ksquirrel-libs-fig2ppm
%{prefix}/bin/ksquirrel-libs-iff2ppm
%{prefix}/bin/ksquirrel-libs-leaf2ppm
%{prefix}/bin/ksquirrel-libs-ljpeg2ppm
%{prefix}/bin/ksquirrel-libs-ljpeg2ppm-s
%{prefix}/bin/ksquirrel-libs-mac2ppm
%{prefix}/bin/ksquirrel-libs-neo2ppm
%{prefix}/bin/ksquirrel-libs-pi12ppm
%{prefix}/bin/ksquirrel-libs-pi32ppm
%if %{with pict}
%{prefix}/bin/ksquirrel-libs-pict2ppm
%endif
%if %{with svg}
%{prefix}/bin/ksquirrel-libs-svg2png
%endif
%if %{with freetype}
%{prefix}/bin/ksquirrel-libs-ttf2pnm
%endif
%{prefix}/bin/ksquirrel-libs-utah2ppm
%{prefix}/bin/ksquirrel-libs-xcf2pnm
%{prefix}/bin/ksquirrel-libs-xim2ppm

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{prefix}/%{_lib}/pkgconfig"

