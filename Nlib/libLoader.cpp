#include "module.h"

// Definitions /////////////////////////////////////////////////////////////////
PyObject* LibrariesException = NULL;

typedef PyObject* (*fpSubmodule)(PyObject*);


// Static declared /////////////////////////////////////////////////////////////
static fpSubmodule subModules[] = {
  PyInit_BasisInitHandler,
  NULL
};


// API implementation //////////////////////////////////////////////////////////
// module initialize
static PyMethodDef module_methods[] = {
    {NULL}  /* Sentinel */
};

PyMODINIT_FUNC
initLibTest(void)
{
    PyObject* m = NULL;
    fpSubmodule* loader = NULL;
    PyObject* s = NULL;

    if(NULL == (LibrariesException = PyErr_NewException("libraries.Exception",
                                                       PyExc_Exception,
                                                       NULL)))
    {
        DEPRINT("NewException");
        return;
    }
    m = Py_InitModule("LibTest", module_methods);

    PyModule_AddObject(m, "LibrariesException", LibrariesException);
  

    for(loader = subModules; *loader != NULL; loader++)
    {
        s = (*loader)(m);

        if(NULL == s)
        {
            Py_DECREF(m);
            return;
        }
    }

    return;
}
