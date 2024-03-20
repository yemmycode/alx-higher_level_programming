#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("  [ERROR] Invalid Python list object\n");
        return;
    }

    Py_ssize_t size = PyList_Size(p);
    Py_ssize_t i;

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List = %ld\n", size);
    printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++) {
        PyObject *item = PyList_GetItem(p, i);
        const char *type = item->ob_type->tp_name;
        printf("Element %ld: %s\n", i, type);
    }
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("  [ERROR] Invalid Python bytes object\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    Py_ssize_t i;

    printf("[.] bytes object info\n");
    printf("  size: %ld\n", size);
    printf("  trying string: %s\n", ((PyBytesObject *)p)->ob_sval);

    printf("  first 10 bytes: ");
    for (i = 0; i < size && i < 10; i++) {
        printf("%02x", ((unsigned char *)p->ob_type)[i]);
        if (i < 9 && i < size - 1)
            printf(" ");
    }
    printf("\n");
}
