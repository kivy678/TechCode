#ifndef __NLIB_INCLUDE_COMMON_MODULE_H__
#define __NLIB_INCLUDE_COMMON_MODULE_H__

#include <Python.h>
#include "common/common.h"


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

#define GET_REFCOUNT(obj, ...)      __GET_REFCOUNT(PyLong_AsLong(PyLong_FromSsize_t(Py_REFCNT(obj))), ##__VA_ARGS__)


#define __EXCEPTION(ret, obj, ...)  PyErr_Format(obj, ##__VA_ARGS__)
#define SPAM_EXCEPTION(ret, ...) 	__EXCEPTION((ret), SpamException, ##__VA_ARGS__)


#endif // __NLIB_INCLUDE_COMMON_MODULE_H__
