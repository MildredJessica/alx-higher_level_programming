#include <Python.h>

/**
 * print_python_list_info - Prints basic info about Python lists.
 * @p: A PyObject list.
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
long int size;
int i;
PyListObject *obj;

size = Py_SIZE(p);
obj = (PyListObject *)p->allocated;
printf("[*] Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", obj);
for (i = 0; i < size; i++)
{
printf("Element %d: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
}
