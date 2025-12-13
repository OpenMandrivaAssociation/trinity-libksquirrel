%bcond clang 1
%bcond ghostscript 1
%bcond djvu 1
%bcond xmedcon 0
%bcond svg 1
%bcond jasper 1
%bcond freetype 1

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
%define tde_prefix /opt/trinity
%define tde_bindir %{tde_prefix}/bin
%define tde_datadir %{tde_prefix}/share
%define tde_docdir %{tde_datadir}/doc
%define tde_includedir %{tde_prefix}/include
%define tde_libdir %{tde_prefix}/%{_lib}
%define tde_mandir %{tde_datadir}/man
%define tde_tdeappdir %{tde_datadir}/applications/tde
%define tde_tdedocdir %{tde_docdir}/tde
%define tde_tdeincludedir %{tde_includedir}/tde
%define tde_tdelibdir %{tde_libdir}/trinity

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

Prefix:			%{tde_prefix}

Source0:	https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{tde_version}/main/libraries/%{tarball_name}-%{tde_version}%{?preversion:~%{preversion}}.tar.xz
Source1:	%{name}-rpmlintrc

BuildSystem:    cmake
BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_SKIP_RPATH=OFF
BuildOption:    -DCMAKE_SKIP_INSTALL_RPATH=OFF
BuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON
BuildOption:    -DCMAKE_INSTALL_RPATH="%{tde_libdir}"
BuildOption:    -DCMAKE_INSTALL_PREFIX="%{tde_prefix}"
BuildOption:    -DSHARE_INSTALL_PREFIX="%{tde_datadir}"
BuildOption:    -DINCLUDE_INSTALL_DIR="%{tde_includedir}"
BuildOption:    -DLIB_INSTALL_DIR="%{tde_libdir}"
BuildOption:    -DWITH_ALL_OPTIONS=ON -DBUILD_ALL=ON -DBUILD_DICOM=OFF
BuildOption:    -DBUILD_PICT=OFFBuildOption:    -DCMAKE_BUILD_WITH_INSTALL_RPATH=ON


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
%dir %{tde_libdir}/ksquirrel-libs
%{tde_libdir}/ksquirrel-libs/libkls_avs.so.0
%{tde_libdir}/ksquirrel-libs/libkls_avs.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_bmp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_bmp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_camera.so.0
%{tde_libdir}/ksquirrel-libs/libkls_camera.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_cut.so.0
%{tde_libdir}/ksquirrel-libs/libkls_cut.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_dds.so.0
%{tde_libdir}/ksquirrel-libs/libkls_dds.so.0.8.0
%if %{with xmedcon}
%{tde_libdir}/ksquirrel-libs/libkls_dicom.so.0
%{tde_libdir}/ksquirrel-libs/libkls_dicom.so.0.8.0
%endif
%if %{with djvu}
%{tde_libdir}/ksquirrel-libs/libkls_djvu.so.0
%{tde_libdir}/ksquirrel-libs/libkls_djvu.so.0.8.0
%endif
%if %{with ghostscript}
%{tde_libdir}/ksquirrel-libs/libkls_eps.so.0
%{tde_libdir}/ksquirrel-libs/libkls_eps.so.0.8.0
%endif
%{tde_libdir}/ksquirrel-libs/libkls_fig.so.0
%{tde_libdir}/ksquirrel-libs/libkls_fig.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_fli.so.0
%{tde_libdir}/ksquirrel-libs/libkls_fli.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_gif.so.0
%{tde_libdir}/ksquirrel-libs/libkls_gif.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_hdr.so.0
%{tde_libdir}/ksquirrel-libs/libkls_hdr.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_ico.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ico.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_iff.so.0
%{tde_libdir}/ksquirrel-libs/libkls_iff.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_jbig.so.0
%{tde_libdir}/ksquirrel-libs/libkls_jbig.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.so.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.so.0
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_koala.so.0
%{tde_libdir}/ksquirrel-libs/libkls_koala.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_leaf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_leaf.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_lif.so.0
%{tde_libdir}/ksquirrel-libs/libkls_lif.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mac.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mac.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mdl.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mdl.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mng.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mng.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_msp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_msp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_mtv.so.0
%{tde_libdir}/ksquirrel-libs/libkls_mtv.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_neo.so.0
%{tde_libdir}/ksquirrel-libs/libkls_neo.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_openexr.so.0
%{tde_libdir}/ksquirrel-libs/libkls_openexr.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pcx.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pcx.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pi1.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pi1.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pi3.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pi3.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pict.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pict.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pix.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pix.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_png.so.0
%{tde_libdir}/ksquirrel-libs/libkls_png.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pnm.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pnm.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_psd.so.0
%{tde_libdir}/ksquirrel-libs/libkls_psd.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_psp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_psp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_pxr.so.0
%{tde_libdir}/ksquirrel-libs/libkls_pxr.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_ras.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ras.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.so.0
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_sct.so.0
%{tde_libdir}/ksquirrel-libs/libkls_sct.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_sgi.so.0
%{tde_libdir}/ksquirrel-libs/libkls_sgi.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_sun.so.0
%{tde_libdir}/ksquirrel-libs/libkls_sun.so.0.8.0
%if %{with svg}
%{tde_libdir}/ksquirrel-libs/libkls_svg.so.0
%{tde_libdir}/ksquirrel-libs/libkls_svg.so.0.8.0
%endif
%{tde_libdir}/ksquirrel-libs/libkls_tga.so.0
%{tde_libdir}/ksquirrel-libs/libkls_tga.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_tiff.so.0
%{tde_libdir}/ksquirrel-libs/libkls_tiff.so.0.8.0
%if %{with freetype}
%{tde_libdir}/ksquirrel-libs/libkls_ttf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_ttf.so.0.8.0
%endif
%{tde_libdir}/ksquirrel-libs/libkls_utah.so.0
%{tde_libdir}/ksquirrel-libs/libkls_utah.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_wal.so.0
%{tde_libdir}/ksquirrel-libs/libkls_wal.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.so.0
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_wmf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_wmf.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xbm.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xbm.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xcf.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xcf.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xcur.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xcur.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xim.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xim.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xpm.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xpm.so.0.8.0
%{tde_libdir}/ksquirrel-libs/libkls_xwd.so.0
%{tde_libdir}/ksquirrel-libs/libkls_xwd.so.0.8.0
%{tde_libdir}/libksquirrel-libs-png.so.0
%{tde_libdir}/libksquirrel-libs-png.so.0.8.0
%{tde_libdir}/libksquirrel-libs.so.0
%{tde_libdir}/libksquirrel-libs.so.0.8.0
%dir %{tde_datadir}/ksquirrel-libs
%{tde_datadir}/ksquirrel-libs/libkls_camera.so.ui
%if %{with djvu}
%{tde_datadir}/ksquirrel-libs/libkls_djvu.so.ui
%endif
%if %{with svg}
%{tde_datadir}/ksquirrel-libs/libkls_svg.so.ui
%endif
%{tde_datadir}/ksquirrel-libs/libkls_tiff.so.ui
%{tde_datadir}/ksquirrel-libs/libkls_xcf.so.ui
%{tde_datadir}/ksquirrel-libs/rgbmap
%{tde_mandir}/man1/ksquirrel-libs-camera2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-dcraw.1
%{tde_mandir}/man1/ksquirrel-libs-dicom2png.1
%{tde_mandir}/man1/ksquirrel-libs-fig2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-iff2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-leaf2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-ljpeg2ppm-s.1
%{tde_mandir}/man1/ksquirrel-libs-ljpeg2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-mac2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-neo2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-pi12ppm.1
%{tde_mandir}/man1/ksquirrel-libs-pi32ppm.1
%{tde_mandir}/man1/ksquirrel-libs-svg2png.1
%{tde_mandir}/man1/ksquirrel-libs-ttf2pnm.1
%{tde_mandir}/man1/ksquirrel-libs-utah2ppm.1
%{tde_mandir}/man1/ksquirrel-libs-xcf2pnm.1
%{tde_mandir}/man1/ksquirrel-libs-xim2ppm.1

##########

%package devel
Group:		Development/Libraries/Other
Summary:	Trinity image viewer
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description devel
This package contains the development libraries for KSquirrel.

%files devel
%defattr(-,root,root,-)
%dir %{tde_includedir}/ksquirrel-libs
%{tde_includedir}/ksquirrel-libs/error.h
%{tde_includedir}/ksquirrel-libs/fileio.h
%{tde_includedir}/ksquirrel-libs/fmt_codec_base.h
%{tde_includedir}/ksquirrel-libs/fmt_defs.h
%{tde_includedir}/ksquirrel-libs/fmt_types.h
%{tde_includedir}/ksquirrel-libs/fmt_utils.h
%{tde_includedir}/ksquirrel-libs/ksquirrel_libs_export.h
%{tde_includedir}/ksquirrel-libs/settings.h
%{tde_libdir}/ksquirrel-libs/libkls_avs.la
%{tde_libdir}/ksquirrel-libs/libkls_avs.so
%{tde_libdir}/ksquirrel-libs/libkls_bmp.la
%{tde_libdir}/ksquirrel-libs/libkls_bmp.so
%{tde_libdir}/ksquirrel-libs/libkls_camera.la
%{tde_libdir}/ksquirrel-libs/libkls_camera.so
%{tde_libdir}/ksquirrel-libs/libkls_cut.la
%{tde_libdir}/ksquirrel-libs/libkls_cut.so
%{tde_libdir}/ksquirrel-libs/libkls_dds.la
%{tde_libdir}/ksquirrel-libs/libkls_dds.so
%if %{with xmedcon}
%{tde_libdir}/ksquirrel-libs/libkls_dicom.la
%{tde_libdir}/ksquirrel-libs/libkls_dicom.so
%endif
%if %{with djvu}
%{tde_libdir}/ksquirrel-libs/libkls_djvu.la
%{tde_libdir}/ksquirrel-libs/libkls_djvu.so
%endif
%if %{with ghostscript}
%{tde_libdir}/ksquirrel-libs/libkls_eps.la
%{tde_libdir}/ksquirrel-libs/libkls_eps.so
%endif
%{tde_libdir}/ksquirrel-libs/libkls_fig.la
%{tde_libdir}/ksquirrel-libs/libkls_fig.so
%{tde_libdir}/ksquirrel-libs/libkls_fli.la
%{tde_libdir}/ksquirrel-libs/libkls_fli.so
%{tde_libdir}/ksquirrel-libs/libkls_gif.la
%{tde_libdir}/ksquirrel-libs/libkls_gif.so
%{tde_libdir}/ksquirrel-libs/libkls_hdr.la
%{tde_libdir}/ksquirrel-libs/libkls_hdr.so
%{tde_libdir}/ksquirrel-libs/libkls_ico.la
%{tde_libdir}/ksquirrel-libs/libkls_ico.so
%{tde_libdir}/ksquirrel-libs/libkls_iff.la
%{tde_libdir}/ksquirrel-libs/libkls_iff.so
%{tde_libdir}/ksquirrel-libs/libkls_jbig.la
%{tde_libdir}/ksquirrel-libs/libkls_jbig.so
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.la
%{tde_libdir}/ksquirrel-libs/libkls_jpeg.so
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.la
%{tde_libdir}/ksquirrel-libs/libkls_jpeg2000.so
%{tde_libdir}/ksquirrel-libs/libkls_koala.la
%{tde_libdir}/ksquirrel-libs/libkls_koala.so
%{tde_libdir}/ksquirrel-libs/libkls_leaf.la
%{tde_libdir}/ksquirrel-libs/libkls_leaf.so
%{tde_libdir}/ksquirrel-libs/libkls_lif.la
%{tde_libdir}/ksquirrel-libs/libkls_lif.so
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.la
%{tde_libdir}/ksquirrel-libs/libkls_ljpeg.so
%{tde_libdir}/ksquirrel-libs/libkls_mac.la
%{tde_libdir}/ksquirrel-libs/libkls_mac.so
%{tde_libdir}/ksquirrel-libs/libkls_mdl.la
%{tde_libdir}/ksquirrel-libs/libkls_mdl.so
%{tde_libdir}/ksquirrel-libs/libkls_mng.la
%{tde_libdir}/ksquirrel-libs/libkls_mng.so
%{tde_libdir}/ksquirrel-libs/libkls_msp.la
%{tde_libdir}/ksquirrel-libs/libkls_msp.so
%{tde_libdir}/ksquirrel-libs/libkls_mtv.la
%{tde_libdir}/ksquirrel-libs/libkls_mtv.so
%{tde_libdir}/ksquirrel-libs/libkls_neo.la
%{tde_libdir}/ksquirrel-libs/libkls_neo.so
%{tde_libdir}/ksquirrel-libs/libkls_openexr.la
%{tde_libdir}/ksquirrel-libs/libkls_openexr.so
%{tde_libdir}/ksquirrel-libs/libkls_pcx.la
%{tde_libdir}/ksquirrel-libs/libkls_pcx.so
%{tde_libdir}/ksquirrel-libs/libkls_pi1.la
%{tde_libdir}/ksquirrel-libs/libkls_pi1.so
%{tde_libdir}/ksquirrel-libs/libkls_pi3.la
%{tde_libdir}/ksquirrel-libs/libkls_pi3.so
%{tde_libdir}/ksquirrel-libs/libkls_pict.so
%{tde_libdir}/ksquirrel-libs/libkls_pict.la
%{tde_libdir}/ksquirrel-libs/libkls_pix.la
%{tde_libdir}/ksquirrel-libs/libkls_pix.so
%{tde_libdir}/ksquirrel-libs/libkls_png.la
%{tde_libdir}/ksquirrel-libs/libkls_png.so
%{tde_libdir}/ksquirrel-libs/libkls_pnm.la
%{tde_libdir}/ksquirrel-libs/libkls_pnm.so
%{tde_libdir}/ksquirrel-libs/libkls_psd.la
%{tde_libdir}/ksquirrel-libs/libkls_psd.so
%{tde_libdir}/ksquirrel-libs/libkls_psp.la
%{tde_libdir}/ksquirrel-libs/libkls_psp.so
%{tde_libdir}/ksquirrel-libs/libkls_pxr.la
%{tde_libdir}/ksquirrel-libs/libkls_pxr.so
%{tde_libdir}/ksquirrel-libs/libkls_ras.la
%{tde_libdir}/ksquirrel-libs/libkls_ras.so
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.la
%{tde_libdir}/ksquirrel-libs/libkls_rawrgb.so
%{tde_libdir}/ksquirrel-libs/libkls_sct.la
%{tde_libdir}/ksquirrel-libs/libkls_sct.so
%{tde_libdir}/ksquirrel-libs/libkls_sgi.la
%{tde_libdir}/ksquirrel-libs/libkls_sgi.so
%{tde_libdir}/ksquirrel-libs/libkls_sun.la
%{tde_libdir}/ksquirrel-libs/libkls_sun.so
%if %{with svg}
%{tde_libdir}/ksquirrel-libs/libkls_svg.la
%{tde_libdir}/ksquirrel-libs/libkls_svg.so
%endif
%{tde_libdir}/ksquirrel-libs/libkls_tga.la
%{tde_libdir}/ksquirrel-libs/libkls_tga.so
%{tde_libdir}/ksquirrel-libs/libkls_tiff.la
%{tde_libdir}/ksquirrel-libs/libkls_tiff.so
%if %{with freetype}
%{tde_libdir}/ksquirrel-libs/libkls_ttf.la
%{tde_libdir}/ksquirrel-libs/libkls_ttf.so
%endif
%{tde_libdir}/ksquirrel-libs/libkls_utah.la
%{tde_libdir}/ksquirrel-libs/libkls_utah.so
%{tde_libdir}/ksquirrel-libs/libkls_wal.la
%{tde_libdir}/ksquirrel-libs/libkls_wal.so
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.la
%{tde_libdir}/ksquirrel-libs/libkls_wbmp.so
%{tde_libdir}/ksquirrel-libs/libkls_wmf.la
%{tde_libdir}/ksquirrel-libs/libkls_wmf.so
%{tde_libdir}/ksquirrel-libs/libkls_xbm.la
%{tde_libdir}/ksquirrel-libs/libkls_xbm.so
%{tde_libdir}/ksquirrel-libs/libkls_xcf.la
%{tde_libdir}/ksquirrel-libs/libkls_xcf.so
%{tde_libdir}/ksquirrel-libs/libkls_xcur.la
%{tde_libdir}/ksquirrel-libs/libkls_xcur.so
%{tde_libdir}/ksquirrel-libs/libkls_xim.la
%{tde_libdir}/ksquirrel-libs/libkls_xim.so
%{tde_libdir}/ksquirrel-libs/libkls_xpm.la
%{tde_libdir}/ksquirrel-libs/libkls_xpm.so
%{tde_libdir}/ksquirrel-libs/libkls_xwd.la
%{tde_libdir}/ksquirrel-libs/libkls_xwd.so
%{tde_libdir}/libksquirrel-libs-png.la
%{tde_libdir}/libksquirrel-libs-png.so
%{tde_libdir}/libksquirrel-libs.la
%{tde_libdir}/libksquirrel-libs.so
%{tde_libdir}/pkgconfig/ksquirrellibs.pc
%{tde_docdir}/ksquirrel-libs/

##########

%package tools
Summary:	Trinity image viewer
Group:		System/Libraries
Requires:	%{name} = %{?epoch:%{epoch}:}%{version}-%{release}

%description tools
This package contains the tools for KSquirrel.

%files tools
%defattr(-,root,root,-)
%{tde_bindir}/ksquirrel-libs-camera2ppm
%{tde_bindir}/ksquirrel-libs-dcraw
%if %{with xmedcon}
%{tde_bindir}/ksquirrel-libs-dicom2png
%endif
%{tde_bindir}/ksquirrel-libs-fig2ppm
%{tde_bindir}/ksquirrel-libs-iff2ppm
%{tde_bindir}/ksquirrel-libs-leaf2ppm
%{tde_bindir}/ksquirrel-libs-ljpeg2ppm
%{tde_bindir}/ksquirrel-libs-ljpeg2ppm-s
%{tde_bindir}/ksquirrel-libs-mac2ppm
%{tde_bindir}/ksquirrel-libs-neo2ppm
%{tde_bindir}/ksquirrel-libs-pi12ppm
%{tde_bindir}/ksquirrel-libs-pi32ppm
%{tde_bindir}/ksquirrel-libs-pict2ppm
%if %{with svg}
%{tde_bindir}/ksquirrel-libs-svg2png
%endif
%if %{with freetype}
%{tde_bindir}/ksquirrel-libs-ttf2pnm
%endif
%{tde_bindir}/ksquirrel-libs-utah2ppm
%{tde_bindir}/ksquirrel-libs-xcf2pnm
%{tde_bindir}/ksquirrel-libs-xim2ppm

%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_bindir}:${PATH}"
export PKG_CONFIG_PATH="%{tde_libdir}/pkgconfig"

