#ifndef __LIB_TABLETYPE_H__
#define __LIB_TABLETYPE_H__

#include <Python.h>
#include <structmember.h>

// BASIS declared /////////////////////////////////////////////////////////////
typedef struct
{
    PyObject_HEAD

    PyObject*       arg_num;
    PyObject*       test_str;

} BASIS;


#endif // __LIB_TABLETYPE_H__
