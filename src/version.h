#ifndef __VERSION_H_
#define __VERSION_H_

// graphn: script/pre_script.py defines these at build time as YY.MM.NN (year, month, and this month's commit
// count, like the goggle firmware's YY.MM.NN-graphn). The values below are only the fallback when it cannot
// (a source tree without git).
#ifndef VTX_VERSION_MAJOR
#define VTX_VERSION_MAJOR       1 // increment when a major release is made (big new feature, etc)
#define VTX_VERSION_MINOR       8 // increment when a minor release is made (small new feature, change etc)
#define VTX_VERSION_PATCH_LEVEL 0 // increment when a bug is fixed
#endif
#ifndef VTX_VERSION_STRING
#define VTX_VERSION_STRING      STR(VTX_VERSION_MAJOR) "." STR(VTX_VERSION_MINOR) "." STR(VTX_VERSION_PATCH_LEVEL)
#endif

#define _STR(x) #x
#define STR(x)  _STR(x)

#endif /* __VERSION_H_ */
