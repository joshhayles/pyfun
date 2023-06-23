# splits the string up into lines and returns them in a list. In other words, escape sequences are removed / ignored

string = "foo\nbar\r\nbaz\fqux\u2028quux"

print(string.splitlines())  # -> ['foo', 'bar', 'baz', 'qux', 'quux']
