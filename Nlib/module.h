#ifndef __LIB_MODULE_H__
#define __LIB_MODULE_H__

#include "common/common.h"
#include "tabletype.h"

using namespace std;


#define PYOBJECT_CHECK(obj, label) 		         \
    if (!obj)							         \
    { 									         \
        PyErr_Print();					         \
        goto label; 					         \
    }

#define __GET_REFCOUNT(obj, ...)           \
    {                                           \
        printf("%d\n", obj, ##__VA_ARGS__);    \
    }

#define GET_REFCOUNT(obj, ...)     		 __GET_REFCOUNT(PyLong_AsLong(PyLong_FromSsize_t(Py_REFCNT(obj))), ##__VA_ARGS__)


#define __EXCEPTION(ret, obj, ...)      PyErr_Format(obj, ##__VA_ARGS__)

#define LIBRARY_EXCEPTION(ret, ...) 	__EXCEPTION((ret), LibrariesException, ##__VA_ARGS__)
#define BASIS_EXCEPTION(ret, ...) 		__EXCEPTION((ret), BasisException, ##__VA_ARGS__)

#ifdef __cplusplus
extern "C"
{
#endif

PyObject* PyInit_BasisInitHandler(PyObject*);


#ifdef __cplusplus
}
#endif


#endif // __LIB_MODULE_H__
