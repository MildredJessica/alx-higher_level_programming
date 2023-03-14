#include <python3.4/Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - Print the basic information about python list
 * @p: Python object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
long int size, alloc;
int i;
Pyobject *obj;

size = PyList_size(p);
obj = (PyListObject *)p;

printf("[*]  Size of the Python List = %li\n", size);
printf("[*] Allocated = %li\n", obj->allocated);
for (i = 0; i < size; i++)
printf("Element %i: %s\n", i, Py_TYPE(obj->ob_item[i])->tp_name);
}
