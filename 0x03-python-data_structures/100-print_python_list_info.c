#include "<Python/Python.h>"

/**
 * print_python_list_info - Print the basic information about python list
 * @p: Python object
 * Return: Nothing
 */
void print_python_list_info(PyObject *p)
{
int size, alloc, i;
Pyobject *obj;

size = Py_size(p);
alloc = ((PyListObject *)p)->allocated;

printf("[*]  Size of the Python List = %d\n", size);
printf("[*] Allocated = %d\n", alloc);
for (i = 0; i < size; i++)
{
printf("Element %d: ", i);
obj = PyList_GetItem(p, i);
print("%s\n", Py_TYPE(obj)->tp_name);
}
}