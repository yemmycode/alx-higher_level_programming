#include <Python.h>
#include <stdio.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

void print_python_list(PyObject *p) {
    if (!PyList_Check(p)) {
        printf("[ERROR] PyListObject is invalid\n");
        return;
    }

    printf("[*] Python list info\n");
    printf("[*] Size of the Python List: %ld\n", PyList_Size(p));
    fflush(stdout);
}

void print_python_bytes(PyObject *p) {
    if (!PyBytes_Check(p)) {
        printf("[ERROR] PyBytesObject is invalid\n");
        return;
    }

    Py_ssize_t size = PyBytes_Size(p);
    const char *bytes = PyBytes_AsString(p);

    printf("[.] bytes object info\n");
    printf("  Size: %ld\n", size);
    printf("  Trying string: %s\n", bytes);

    printf("[*] First %ld bytes: ", (size < 10) ? size : 10);
    for (Py_ssize_t i = 0; i < ((size < 10) ? size : 10); i++) {
        printf("%02hhx", bytes[i]);
        if (i < ((size < 10) ? size - 1 : 9)) {
            printf(" ");
        }
    }
    printf("\n");
    fflush(stdout);
}

void print_python_float(PyObject *p) {
    if (!PyFloat_Check(p)) {
        printf("[ERROR] PyFloatObject is invalid\n");
        return;
    }

    double value = PyFloat_AsDouble(p);

    printf("[.] float object info\n");
    printf("  Value: %.17g\n", value);
    fflush(stdout);
}
