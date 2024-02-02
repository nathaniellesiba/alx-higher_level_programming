#include <Python.h>

void print_python_string(PyObject *p)
{
    printf("[.] string object info\n");
    if (!PyUnicode_Check(p))
    {
        printf("  [ERROR] Invalid String Object\n");
        return;
    }

    Py_ssize_t len;
    const wchar_t *str = PyUnicode_AsWideCharString(p, &len);

    if (str == NULL)
    {
        printf("  [ERROR] Failed to retrieve string\n");
        return;
    }

    const char *type = PyUnicode_IS_COMPACT_ASCII(p) ? "compact ascii" : "compact unicode object";

    printf("  type: %s\n", type);
    printf("  length: %ld\n", len);
    wprintf(L"  value: %ls\n", str);

    PyMem_Free((void *)str);  // Free the memory allocated by PyUnicode_AsWideCharString
}

